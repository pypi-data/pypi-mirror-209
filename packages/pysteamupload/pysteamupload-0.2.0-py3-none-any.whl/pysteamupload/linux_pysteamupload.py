import os
import tarfile
from abc import abstractmethod
from pysteamupload.generic_pysteamupload import GenericPySteamUpload


class LinuxPySteamUpload(GenericPySteamUpload):
    @abstractmethod
    def get_steamcmd_local_filename(self) -> str:
        return "steamcmd.sh"

    @abstractmethod
    def get_steamcmd_remote_filename(self) -> str:
        return "steamcmd_linux.tar.gz"

    @abstractmethod
    def extract_steamcmd_archive(self) -> None:
        with tarfile.open(self.get_archive_path(), 'r:gz') as f:
            self._safe_extract(tar_file_handler=f, path=str(self.root_directory))

    @staticmethod
    def _is_within_directory(directory: str, target: str) -> bool:
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
        prefix = os.path.commonprefix([abs_directory, abs_target])
        return prefix == abs_directory

    @staticmethod
    def _safe_extract(tar_file_handler, path: str, members=None, *, numeric_owner=False) -> None:
        for member in tar_file_handler.getmembers():
            member_path = os.path.join(path, member.name)
            if not LinuxPySteamUpload._is_within_directory(path, member_path):
                raise RuntimeError("Attempted Path Traversal in Tar File")
        tar_file_handler.extractall(path, members, numeric_owner=numeric_owner)
