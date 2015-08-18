# Architecture

`ImageMachine` is a very simple python program.

It does the following things:

- Retrieves files from an FTP
- Grabs the image urls to be downloaded
- Downloads the images and compresses them into a file.

This functionality is scattered between the following classes:

- `FtpClient`
- `ImageCsv`

In addition, there are a few helper modules such as the `settings` and
the `util` modules.

The `settings` module is what reads from a JSON file named `config.json` to
store credentials or debugging options. The `config.json` should live within
the `image_machine`. Refer to `config.json.example` for how it should be
structured.

