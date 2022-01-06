from main import ALL_SERVICE_INDICES, get_services_bits_enc, get_services_from_bits_enc


def test_small_list_of_services():
    sm = [1062, 1258, 2869]
    enc = get_services_bits_enc(sm)
    result = get_services_from_bits_enc(enc)
    assert result == sm
    print("pass")


def test_lg_list_of_services():
    lg = [svc_id for svc_id, ix in ALL_SERVICE_INDICES]
    enc = get_services_bits_enc(lg)
    assert len(enc) < 200  # it's short
    result = get_services_from_bits_enc(enc)
    assert result == lg
    print("pass")


if __name__ == "__main__":
    test_small_list_of_services()
    test_lg_list_of_services()
