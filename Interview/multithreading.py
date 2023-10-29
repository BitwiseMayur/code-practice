"""
Basic illustration of a multithreading

Scenario: We have a scenario where in a user tries to download a report on the UI. The bigger the report the time it takes, the user will not know whether the process is running or it has stopped. To address the scenario, the implementation was to create a separate thread based on the number of cells in the excel, fox ex: if the number of cells > 2,00,000 then create a separate thread and shoe a msg on the UI. Then later once the thread is completed send the excel file to the email address.
"""

import threading

def process(req):
    # Main function where in we get the request to download the report
    # Check the number of cells, if the cells are > 200000 then create a thread
    dto = json.loads(req)
    num_of_cells = get_no_of_cells(dto)

    if num_of_cells > some_limit:    # Limit is mentioned in the config file
        t = threading.Thread(target=send_email_with_link, args=(dto,))

        t.start()    # The thread will start, we are not using t.join() to wait as the request will be async

        return json.dumps({"message":"Sending excel with link"}), 200, {}

    download_token = grid_export(dto)
    return json.dumps({"download_token":download_token, "status":1, "message": ""}), 200, {}

def send_email_with_link(response_dto):
    lock.acquire() # Acquire the lock

    try:
        # Prepare the excel and send the excel
        pass
    except Exception as e:
        # log the error
    finally:
        lock.release()
