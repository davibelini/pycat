# pycat is my version of unix systems 'cat' command, written in python.

> ## How to obtain pycat:
- From Github:
    - Open your terminal.
    - Clone the repository:
    ```sh
    git clone https://github.com/davibelini/pycat.git/
    ```
    - Navigate to the repository:
    ```sh
    cd pycat
    ```
- From the website:
    - Not yet available.
> ## Docs >
- ### Commands:
    - #### read -> 
        - ###### SYNTAX: 
        ```sh
        pycat read <filepath>
        ```
        - ###### DESCRIPTION: prints the content of a readable file to the console.
    - #### write -> 
        - ###### SYNTAX: 
        ```sh
        pycat write <filepath> "<text>"
        ```
        - ###### DESCRIPTION: appends new content to an ascii file.
    - #### make ->
        - ###### SYNTAX: 
        ```sh
        pycat make <filename>
        ```
        - ###### DESCRIPTION: creates an empty file.
    - #### join ->
        - ###### SYNTAX: 
        ```sh
        pycat join <filepath> <filepath>
        ```
        - ###### DESCRIPTION: copies second argument file content to another existing file.
        