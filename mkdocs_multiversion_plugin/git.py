# -*- coding: utf-8 -*-
import logging
import subprocess
import collections
import re

logger = logging.getLogger(__name__)

GitData = collections.namedtuple(
    'Version',
    [
        'name',
        'source',
        'is_remote',
        'refname',
    ],
)


class Git:
    @staticmethod
    def get_name(cwd=None) -> str:
        """
        Extracts the branch or tag name from git repo

        Returns:
            str: Returns the branch or tag name from repo as a string.
        """
        try:
            cmd = (
                'git',
                'symbolic-ref',
                '-q',
                '--short',
                'HEAD'
            )
            output = subprocess.check_output(cmd, cwd=cwd).decode()
            return output.rstrip("\n")
        except Exception as e:
            try:
                logger.debug("It's not a branch, get the tag name")
                cmd = (
                    'git',
                    'describe',
                    '--tags',
                    '--exact-match'
                )
                output = subprocess.check_output(cmd, cwd=cwd).decode()
                return output.rstrip("\n")
            except Exception as ex:
                logger.debug("It's not a tag, detached state")
                cmd = (
                    'git',
                    'branch',
                    '--remote',
                    '--no-abbrev',
                    '--contains'
                )
                output = subprocess.check_output(cmd, cwd=cwd).decode()
                return output.split('/')[-1].rstrip("\n")
  

    @staticmethod
    def get_all_refs():
        """
        Extracts the information on each ref.

        Yields:
            GitData: The next ref information.
        """
        cmd = (
            'git',
            'for-each-ref',
            '--format',
            '%(refname)',
            '--sort',
            'creatordate',
            'refs',
        )
        output = subprocess.check_output(cmd, cwd=None).decode()
        for line in output.splitlines():
            is_remote = False
            fields = line.strip().split("\t")
            if len(fields) != 1:
                continue

            refname = fields[0]

            # Parse refname
            matchobj = re.match(
                r"^refs/(heads|tags|remotes/[^/]+)/(\S+)$", refname
            )
            if not matchobj:
                continue
            source = matchobj.group(1)
            name = matchobj.group(2)

            if source.startswith("remotes/"):
                is_remote = True

            yield GitData(name, source, is_remote, refname)

    @staticmethod
    def get_refs(tag_whitelist, branch_whitelist):
        """
        Retrieves filtered information about refs.

        Yields:
            GitData: The next ref information.
        """
        for ref in Git.get_all_refs():
            if ref.source == "tags":
                if tag_whitelist is None or not re.match(tag_whitelist, ref.name):
                    logger.debug(
                        "Skipping '%s' because tag '%s' doesn't match the "
                        "whitelist pattern",
                        ref.refname,
                        ref.name,
                    )
                    continue
            elif ref.source == "heads":
                if branch_whitelist is None or not re.match(
                    branch_whitelist, ref.name
                ):
                    logger.debug(
                        "Skipping '%s' because branch '%s' doesn't match the "
                        "whitelist pattern",
                        ref.refname,
                        ref.name,
                    )
                    continue
            else:
                logger.debug(
                    "Skipping '%s' because its not a branch or tag", ref.refname
                )
                continue
            yield ref
