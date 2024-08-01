def main():
    def get_book_text(path):
        with open(path) as f:
            return f.read()

    def wordcount(contents):
        words = contents.split()
        return len(words)
    
    def get_character_count(contents):
        low = contents.lower()
        cha = {}
        for c in low:
            if c in cha:
                cha[c] += 1
            else:
                cha[c] = 1
        return cha
    
    def sort_on(d):
        return d["num"]
    
    def sorting(dic):
        sorted_list = []
        for k in dic:
            if k.isalpha():
                sorted_list.append({"char": k, "num" : dic[k]})
        sorted_list.sort(reverse = True, key = sort_on)
        return sorted_list

    def report(path):
        contents = get_book_text(path)
        word_count = wordcount(contents)
        character_count = sorting(get_character_count(contents))

        print(f"--- Begin report of {path} ---")
        print(f"{word_count} words found in the document")
        print()

        for item in character_count:
            print(f"The '{item["char"]}' character was found {item["num"]} times")
        
        print("--- End report ---")

    

    path = "books/frankenstein.txt"
    report(path)

main()