from abc import ABCMeta
from github_repo_scanner.controllers import Main


class TreeStructure(Main, metaclass=ABCMeta):
    pattern = r"/repo/tree/structure"

    async def get(self):
        response = {}
        self.set_status(self.http_status.OK)
        await self.finish(chunk=response)
        return


__all__ = ["TreeStructure"]
