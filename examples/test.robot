*** Settings ***
Library       Remote    http://${ADDRESS}:${PORT}
Library       RemoteTransfer

*** Variables ***
${ADDRESS}    127.0.0.1
${PORT}       8270


*** Test Cases ***
Try Out Remote Transfer
  ${results}=   Remote.Transfer Files  *.png
  RemoteTransfer.Save Files  ${results}
