import re
import random
import string
import time
import regex
import os

class RandomDataTypeGenerator:
    def __init__(self):
        self.generator_options = [self.random_string, self.random_int]

    def get_random(self):
        return random.choice(self.generator_options)()

    def random_string(self, length=79):
        return "".join(
            random.choice(string.ascii_letters)
            for i in range(length)
        )

    def random_int(self):
        return random.randint(0, 999)

class VariableNameGenerator:
    def __init__(self):
        self.generator_options = [
            self.random_string,
            self.l_and_i,
            self.time_based,
            self.just_id,
            self.scream,
            self.single_letter_a_lot,
        ]

    def get_random(self, id):
        return random.choice(self.generator_options)(id)

    def random_string(self, id, length=79):
        return "".join(random.choice(string.ascii_letters) for i in range(length)) + str(id)

    def l_and_i(self, id):
        return "".join(random.choice("Il") for i in range(id))

    def time_based(self, id):
        return random.choice(string.ascii_letters) + str(time.time()).replace(".", "") + str(id)

    def just_id(self, id):
        return random.choice(string.ascii_letters) + str(id)

    def scream(self, id):
        return "".join(random.choice("Aa") for i in range(id))

    def single_letter_a_lot(self, id):
        return random.choice(string.ascii_letters) * id

def one_liner(code):
    formatted_code = re.sub(
        r"(;)\1+",
        ";",
        """exec(\"\"\"{};\"\"\")""".format(
            code.replace("\n", ";").replace('"""', '\\"\\"\\"')
        ),
    )

    if formatted_code[0] == ';':
        return formatted_code[1:]
    return formatted_code

def variable_renamer(code):
    code = "\n" + code
    variable_names = re.findall(r"(\w+)(?=( |)=( |))", code)
    name_generator = VariableNameGenerator()
    for i in range(len(variable_names)):
        obfuscated_name = name_generator.get_random(i + 1)
        code = re.sub(
            r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_name, code
        )
    return code

def add_random_variables(code):
    useless_variables_to_add = random.randint(100, 400)
    name_generator = VariableNameGenerator()
    data_generator = RandomDataTypeGenerator()
    for v in range(1, useless_variables_to_add):
        rand_data = data_generator.get_random()
        if type(rand_data) == str:
            rand_data = '"{}"'.format(rand_data)
        if v % 2 == 0:
            code = "{} = {}\n".format(name_generator.get_random(v), rand_data) + code
        else:
            code = code + "\n{} = {}".format(name_generator.get_random(v), rand_data)
    return code

def str_to_hex_bytes(code):
    python_string_decoraters = ['"""', "'''", '"', "'"]

    for s in python_string_decoraters:
        pattern = r"((?<=(( |	|\n)\w+( |)=( |))({}))[\W\w]*?(?=({})))".format(s, s)
        t = regex.findall(pattern, code)
        for v in t:
            string_contents = v[0]
            if s == '"' and string_contents == '"':
                continue
            if s == "'" and string_contents == "'":
                continue
            hex_bytes = "\\" + "\\".join(
                x.encode("utf-8").hex() for x in string_contents
            )
            code = regex.sub(pattern, str(hex_bytes).replace("\\", "\\\\"), code)

    return code

def obfuscate(code, remove_techniques=[]):
    if len(remove_techniques) == 0:
        methods = all_methods
    else:
        methods = all_methods.copy()
        for technique in remove_techniques:
            methods.remove(technique)

    for technique in methods:
        code = technique(code)

    return code

all_methods = [variable_renamer, add_random_variables, one_liner, str_to_hex_bytes]

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    input_file = input("Enter the path of the file to obfuscate: ")
    
    if not os.path.isfile(input_file):
        print("File not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        code = file.read()

    obfuscated_code = obfuscate(code)

    output_file = os.path.join(os.path.dirname(input_file), "obfuscated_" + os.path.basename(input_file))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(obfuscated_code)

    print(f"Obfuscated code saved to {output_file}")

if __name__ == "__main__":
    main()

