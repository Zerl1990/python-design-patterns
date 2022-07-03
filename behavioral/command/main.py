from behavioral.command.commands.create import CreateFileCommand
from behavioral.command.commands.delete import DeleteFileCommand
from behavioral.command.commands.read import ReadFileCommand
from behavioral.command.commands.rename import RenameFileCommand

if __name__ == "__main__":
    file_path = "test.txt"
    dst_path = "test_copy.txt"
    create_cmd = CreateFileCommand(file_path, "TEST TEST TEST")
    read_cmd = ReadFileCommand(file_path)
    rename_cmd = RenameFileCommand(file_path, dst_path)
    delete_cmd = DeleteFileCommand(file_path)

    create_cmd.execute()
    delete_cmd.execute()
    delete_cmd.undo()
    print(read_cmd.execute())
    rename_cmd.execute()
    rename_cmd.undo()
    print(read_cmd.execute())
