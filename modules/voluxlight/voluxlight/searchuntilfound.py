import lifxlan


def search_until_found(name_list, attempts=10):

    lifx = lifxlan.LifxLAN()
    name_found = {name: False for name in name_list}
    devices = []

    for attempt in range(attempts):

        for i, name in enumerate(name_list):

            device_name = name_list[int(i)]
            device_found = name_found[device_name]

            if device_found is True:

                pass
                # print("device already found...")

            elif device_found is False:

                result = lifx.get_device_by_name(device_name)

                if result is None:

                    print(
                        "couldn't find '{}', {} attempts left".format(
                            device_name, attempts - attempt - 1
                        )
                    )

                else:

                    devices.append(result)
                    name_found[device_name] = True
                    print("found '{}'!".format(device_name))

            else:

                raise TypeError("device_found must be a boolean")

    return devices
