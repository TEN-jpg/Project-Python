import os
import shutil

class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.history = []

        if not os.path.exists(self.folder_path):
            raise ValueError(f"Folder does not exist: {self.folder_path}")
        print("----------------------------------------")
        print(f"Folder validated: {self.folder_path}")
        print("-----------------------------------------")

    def get_files(self):
        try:
            all_items = os.listdir(self.folder_path)
            files = []

            for item in all_items:
                item_path = os.path.join(self.folder_path, item)

                if os.path.isfile(item_path):
                    files.append(item)

            return files

        except Exception as e:
            print("Error reading folder:", e)
            return []

    def get_category(self, filename):
        categories = {
            "Images": ["jpg", "jpeg", "png", "gif", "webp"],
            "Videos": ["mp4", "mkv", "webm", "mov"],
            "Documents": ["pdf", "txt", "docx", "xlsx", "csv"],
            "Audio": ["mp3", "wav"],
            "Archives": ["zip", "rar", "7z", "tar"],
            "Code": ["py", "cpp", "html", "css", "js"]
        }

        extension = filename.split(".")[-1].lower() #Just pick the extension of the filename eg:- ".jpg"

        for category, extensions in categories.items():
            if extension in extensions:
                return category

        return "Others"

    def create_folder(self, category):
        destination_folder = os.path.join(self.folder_path, category)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder) #creates a folder

        return destination_folder

    def move_file(self, filename, destination_folder):
        try:
            source_path = os.path.join(self.folder_path, filename)
            destination_path = os.path.join(destination_folder, filename)

            self.history.append((source_path, destination_path))

            shutil.move(source_path, destination_path) #shutil module in Python provides a set of high-level file operations, often referred to as "shell utilities". It is part of the Python standard library and allows you to automate tasks such as copying, moving, renaming, and deleting entire files and directories.

        except Exception as e:
            print("Error moving file:", e)

    def organize(self):
        try:
            files = self.get_files()

            if not files:
                print("No files found to organize.")
                return

            summary_data = {}

            for file in files:
                category = self.get_category(file)
                folder_path = self.create_folder(category)
                self.move_file(file, folder_path)

                print(f"Moved: {file} → {category}")

                summary_data[category] = summary_data.get(category, 0) + 1

            self.summary(summary_data)

        except Exception as e:
            print("Error while organizing files:", e)

    def summary(self, summary_data):
        print("\n------- Organization Complete! --------")
        total_files = sum(summary_data.values())
        print(f"Total Files Organized: {total_files}\n")

        for category, count in summary_data.items():
            print(f"{category}: {count}")

        print("---------------------------------------")
    
    def undo(self):
        try:
            if not self.history:
                print("Nothing to Undo!")
                return
            
            print("\nUndoing last organization...")

            for source_path,destination_path in reversed(self.history):
                if os.path.exists(destination_path):
                    shutil.move(destination_path, source_path)
                    print(f"Resorted: {os.path.basename(source_path)}") #the basename will just extract filename from source_path to be printed

            self.history.clear()

            print("Undo Complete!")

        except Exception as e:
            print("Error undoing changes:", e)
 
def menu():
    organizer = None   # Will be created when user enters a valid folder

    while True:
        print("\n===== FILE ORGANIZER =====")
        print("1. Organize Files")
        print("2. Undo Last Operation")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            folder_path = input("Enter folder path to organize: ")

            try:
                organizer = FileOrganizer(folder_path)
                organizer.organize()
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            if organizer is None:
                print("Error: No organizer session found! Run option 1 first.")
            else:
                organizer.undo()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()

