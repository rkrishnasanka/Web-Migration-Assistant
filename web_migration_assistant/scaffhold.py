from pathlib import Path
from web_migration_assistant.vue_to_react_pipeline import convert


def main():
    input_dir = "/root/sandbox/Web-Migration-Assistant/input/agriworks_portal-master/src"

    output_dir = Path("output")
    if not output_dir.exists():
        Path(output_dir).mkdir()

    # Step 1: Go through the folders and subfolders and find all the files that end with .vue
    for file_path in Path(input_dir).rglob("*.vue"):
        # Step 2: Read the contents of the file
        print(f"Converting: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file_ptr:
            contents = file_ptr.read()
        # Step 3: Pass the contents of the file to the convert function
        new_code, story_code = convert(contents)
        # Step 4: Write the output of the convert function to a new file with the same name but with .tsx extension in the output directory
        output_file_path = Path(output_dir) / file_path.relative_to(input_dir)
        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        output_file_path = output_file_path.with_suffix(".tsx")
        # Generate the storybook file
        story_file_path = output_file_path.with_suffix(".stories.tsx")
        with open(output_file_path, "w", encoding="utf-8") as file_ptr:
            file_ptr.write(new_code)

        with open(story_file_path, "w", encoding="utf-8") as file_ptr:
            file_ptr.write(story_code)


if __name__ == "__main__":
    main()