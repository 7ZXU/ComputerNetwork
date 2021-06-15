# Web server 
It handles one HTTP request at a time

## How to run
1. web server accept and parse the HTTP request
2. get the requested file from the server’s file system
3. create an HTTP response message consisting of the requested file preceded by header lines
4. send the response directly to the client.

※ If the requested file does not present in the server, the server should send an HTTP “404 Not Found” message back to the client

[📝Notion](https://www.notion.so/Problem3-a0c045261f194ccbaaf693bd76ca7a0b)
