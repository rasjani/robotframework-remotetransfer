robotframework-remotetransfer
=============================

Very small keyword library to allow transfering log files like screenshots
between host running a robotframework and robotremoteserver

Usage:

* Load remotetransfer library into python remote server and into robot framework.
* Use `Transfer Files` keyword to load files from output directory and save
  the results into a dict variable.
* Use `Save Files` to store those back into output directory.

This works by providing a library prefix to the keyword do denote where files are
transfered from and save to, like this:

```
*** Settings ***
Library       Remote    http://127.0.0.1:8270
Library       RemoteTransfer

*** Test Cases ***
Try Out Remote Transfer
  ${results}=   Remote.Transfer Files  *.png
  RemoteTransfer.Save Files  ${results}
```

Library uses base64 encoding to transfer files over robot's rpc interface - so keep
that in mind - filetransfers can grow pretty large.


