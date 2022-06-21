import requests
from termcolor import colored

cat_param_1 = 'wtf'
cat_param_2 = ''
car_jpeg = '595f280f557291a9750ebfb7'
cat_says = 'says/something?color=color'
cat_json = 'json=true'


def assert_test(endpoint: object,
                error_code: object = int,
                site: object = type(str)) -> object:
    url = site.format(endpoint)
    response = requests.request("GET", url)
    print("TESTING: ", endpoint)
    try:
        assert response.status_code == error_code
    except AssertionError:
        print(colored("[ERROR] ", "red"),
              colored("Assertion: " + str(error_code), "red"),
              colored("| Result: " + str(response), "red"),
              colored(url, "red"))
        print("\n")
        return
    else:
        print(colored("[OK] ", "green"),
              colored("Assertion: " + str(error_code), 'green'),
              colored("| Result: " + str(response), "green"),
              colored(url, "green"))
        print("\n")


assert_test(cat_param_1, 200, 'https://cataas.com/cat/{}')
assert_test(cat_param_1, 404, 'https://cataas.com/cat/{}')

assert_test(cat_param_2, 200, 'https://cataas.com/cat/{}')
assert_test(cat_param_2, 404, 'https://cataas.com/cat/{}')

assert_test(car_jpeg, 200, 'https://cataas.com/cat/{}')
assert_test(car_jpeg, 404, 'https://cataas.com/cat/{}')

assert_test(cat_says, 200, 'https://cataas.com/cat/{}')
assert_test(cat_says, 404, 'https://cataas.com/cat/{}')

assert_test(cat_json, 200, 'https://cataas.com/cat?{}')
assert_test(cat_json, 404, 'https://cataas.com/cat?{}')
