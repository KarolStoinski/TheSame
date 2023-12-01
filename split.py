def split_file(original_file, keywords):
    file_count = 1
    output_file = None

    with open(original_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Check if line starts with any of the keywords
            if any(line.startswith(keyword) for keyword in keywords):
                if output_file:
                    output_file.close()
                output_file = open(f'splitted/split_{file_count}.txt', 'w', encoding='utf-8')
                file_count += 1
            if output_file:
                output_file.write(line)

    if output_file:
        output_file.close()

# Keywords to look for
keywords = ["Poseł", "Marszałek", "Przedstawiciel Komitetu", "Wicemarszałek", "Minister", "Zastępca Przedstawiciela", "Podsekretarz Stanu", "Prezes Rady Ministrów"]

# Splitting the file
split_file('01_f_ksiazka.txt', keywords)
