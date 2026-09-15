from time import perf_counter
from datetime import date
from random import shuffle

def create_random():
    a = [0] * 50
    for i in range(50):
        a[i] = i
    shuffle(a)
    return a

def get_answer(power):
    num_part = 2 ** (power%10)
    char_part = ""
    match power//10:
        case 1:
            char_part = "k"
        case 2:
            char_part = "m"
        case 3:
            char_part = "b"
        case 4:
            char_part = "t"
    return f"{num_part}{char_part}"


def main():
    with open("log.txt", "a") as log_file:
        rand_power = create_random()
        wrong_answers = 0
        date_today = date.today()
        log_file.write(f"#\n{date_today}\n#\n\n")
        initial_time = perf_counter()
        for i in range(50):
            power = rand_power[i]
            answer = get_answer(power)
            prompt = f"What is 2 ** {power}? "
            user_answer = input(prompt)
            log_file.write(f"{prompt} {user_answer}\n")
            while user_answer != answer:
                wrong_answers += 1
                prompt = f"Wrong! What is 2 ** {power}? "
                user_answer = input(prompt)
                log_file.write(f"{prompt} {user_answer}\n")
        end_time = perf_counter()
        total_time = int(end_time - initial_time)
        print(f"\nYour total time was {total_time} seconds. You answered incorrectly {wrong_answers} times.\n")
        log_file.write(f"\nYour total time was {total_time} seconds. You answered incorrectly {wrong_answers} times.\n\n")


if __name__ == "__main__":
    main()