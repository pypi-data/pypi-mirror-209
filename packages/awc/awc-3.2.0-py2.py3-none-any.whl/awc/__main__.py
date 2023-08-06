#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""awc cli"""

from warnings import filterwarnings as filter_warnings

import awc
import awc.api


def main() -> int:
    """entry / main function"""

    comments: awc.Awc = awc.Awc("http://127.0.0.1:5000", "hello world")

    print(awc.api.total(comments))
    # print(awc.api.post_comment(comments, "a" * 1000000))
    print(awc.api.get_comments(comments, 10000, 10002))
    # print(awc.api.get_comment(comments, 1000))

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    raise SystemExit(main())
