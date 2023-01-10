import shutil
import time

width = shutil.get_terminal_size()[0]
print(f"Detected console width: {width}")


def limit_output(stuff_to_print, prefix="", suffix=""):

    free_length = width - len(prefix) - len(suffix)
    print(f"{prefix}{stuff_to_print:{free_length}.{free_length}}{suffix}", end="\r")


for n in range(10):
    time.sleep(0.5)
    limit_output("Meow Moo Bark" * (10 - n), f"Iteration {n} / ", "/ Nice suffix")

print()  