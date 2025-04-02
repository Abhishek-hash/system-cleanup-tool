import os
import shutil
import subprocess
import sys
import ctypes  # For admin privilege check

# Paths to clean
CLEANUP_PATHS = [
    os.environ.get('TEMP'),        # %temp%
    r'C:\Windows\Temp',            # temp
    r'C:\Windows\Prefetch'         # prefetch
]

def is_admin():
    """Check if the script is running with admin rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Relaunch the script with admin rights if not already elevated."""
    if not is_admin():
        script = sys.argv[0]
        params = ' '.join(sys.argv[1:])
        try:
            subprocess.run(["powershell", "Start-Process", "python", f'"{script}"', "-Verb", "RunAs"] + params.split(), check=True)
        except Exception as e:
            print("Failed to relaunch with admin rights. Please run manually as administrator.")
        sys.exit()

def clear_folder(path):
    deleted_files = []  # Track deleted files
    skipped_files = []  # Track skipped files

    if os.path.exists(path):
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    try:
                        shutil.rmtree(item_path, ignore_errors=False)
                        deleted_files.append(item_path)
                    except Exception:
                        skipped_files.append(item_path)
                else:
                    try:
                        os.remove(item_path)
                        deleted_files.append(item_path)
                    except PermissionError:
                        skipped_files.append(item_path)
                        print(f"Skipping (in-use): {item_path}")

            print(f"Successfully cleaned: {path}")
            # Show detailed logs
            if deleted_files:
                print(f"\nSuccessfully deleted files in: {path}")
                for file in deleted_files:
                    print(f" - {file}")

            if skipped_files:
                print(f"\nSkipped (in-use or permission denied) in: {path}")
                for file in skipped_files:
                    print(f" - {file}")

        except Exception as e:
            print(f"Failed to clean {path}: {e}")
    else:
        print(f"Path not found: {path}")

def run_disk_cleanup():
    try:
        subprocess.run("cleanmgr", check=True)
        print("Disk Cleanup launched successfully.")
    except Exception as e:
        print(f"Failed to launch Disk Cleanup: {e}")

def main():
    if not is_admin():
        run_as_admin()
        return  # Prevents further execution until admin mode is confirmed

    print("Select cleanup option:")
    print("1. Clean Temp, %temp%, and Prefetch")
    print("2. Run Disk Cleanup")
    print("3. Both (Full Cleanup)")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        for path in CLEANUP_PATHS:
            clear_folder(path)
    elif choice == "2":
        run_disk_cleanup()
    elif choice == "3":
        for path in CLEANUP_PATHS:
            clear_folder(path)
        run_disk_cleanup()
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
