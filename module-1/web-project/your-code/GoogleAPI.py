import json
import time
import urllib.error
import urllib.parse
import urllib.request
#https://developers.google.com/places/web-service/search?hl=es#find-place-examples

class GooglePlaces:
    API_KEY = "AIzaSyDyA7AmKOOKKmq5Ww7EtDN6Kb2cGOVWvHU"
    PLACE_SEARCH_BASE_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    @staticmethod
    def place_search(search_value):
        # Join the parts of the URL together into one string.
        params = "+".join(search_value.split()) + "&key=" + GooglePlaces.API_KEY
        url = f'''{GooglePlaces.PLACE_SEARCH_BASE_URL}query="{params}'''
        # print(f"place search request (url: {url})")
        current_delay = 0.1  # Set the initial retry delay to 100ms.
        max_delay = 5  # Set the maximum retry delay to 5 seconds.

        while True:
            try:
                # Get the API response.
                response = urllib.request.urlopen(url)
            except urllib.error.URLError:
                pass  # Fall through to the retry loop.
            else:
                # If we didn't get an IOError then parse the result.
                result = json.load(response)

                if result["status"] == "OK":
                    # return result["results"]
                    next_page_token = result["next_page_token"] if "next_page_token" in result else ""
                    return_values = []
                    for single in result["results"]:
                        name = single["name"].lower() if "name" in single else ""
                        rating = single["rating"]/5 if "rating" in single else ""
                        #types = single["types"] if "types" in single else ""
                        price_level = single["price_level"] if "price_level" in single else ""
                        geometry = single["geometry"]["location"] if "geometry" in single else ""
                        return_values.append([name, rating, price_level, geometry])
                    return [return_values, next_page_token]
                elif result["status"] != "UNKNOWN_ERROR":
                    # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
                    # ZERO_RESULTS. There is no point retrying these requests.
                    raise Exception(result["error_message"])

            if current_delay > max_delay:
                raise Exception("Too many retry attempts.")

            print("Waiting", current_delay, "seconds before retrying.")

            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.

    @staticmethod
    def next_place_search(next_page_token):
        url = f"{GooglePlaces.PLACE_SEARCH_BASE_URL}pagetoken={next_page_token}&key={GooglePlaces.API_KEY}"
        # print(f"place search request (url: {url})")
        current_delay = 0.1  # Set the initial retry delay to 100ms.
        max_delay = 5  # Set the maximum retry delay to 5 seconds.

        while True:
            try:
                # Get the API response.
                response = urllib.request.urlopen(url)
            except urllib.error.URLError:
                pass  # Fall through to the retry loop.
            else:
                # If we didn't get an IOError then parse the result.
                result = json.load(response)
                # print(result)
                if result["status"] == "OK":
                    next_page_token = result["next_page_token"] if "next_page_token" in result else ""
                    return_values = []
                    for single in result["results"]:
                        name = single["name"].lower() if "name" in single else ""
                        rating = single["rating"]/5 if "rating" in single else ""
                        #types = single["types"] if "types" in single else ""
                        price_level = single["price_level"] if "price_level" in single else ""
                        geometry = single["geometry"]["location"] if "geometry" in single else ""
                        return_values.append([name, rating, price_level, geometry])
                    return [return_values, next_page_token]
                elif result["status"] != "UNKNOWN_ERROR":
                    # Many API errors cannot be fixed by a retry, e.g. INVALID_REQUEST or
                    # ZERO_RESULTS. There is no point retrying these requests.
                    raise Exception(result["error_message"])

            if current_delay > max_delay:
                raise Exception("Too many retry attempts.")

            print("Waiting", current_delay, "seconds before retrying.")

            time.sleep(current_delay)
            current_delay *= 2  # Increase the delay each time we retry.

    @staticmethod
    def get_places_list(barrio, ciudad, pais):
        ps = GooglePlaces.place_search(f"restaurants in {barrio} {ciudad} {pais}")
        places = ps[0]
        while True:
            time.sleep(3)
            if ps[1] != "":
                ps = GooglePlaces.next_place_search(ps[1])
                places += ps[0]
            else:
                break

        # print(f"Place search results: {len(places)}")
        # print(f"Place search: {places}")
        return places
