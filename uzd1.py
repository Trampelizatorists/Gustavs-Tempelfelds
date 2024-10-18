while True:

    ievads = int(input("Ievadi savu vecumu: "))
    
    # es nemaku kert string errorus
        


    if ievads <= 0 or ievads > 115:
        print("Tu varbūt neeksistē")

    elif ievads < 13:
        print(f"Tavs vecums ir {ievads}, tu esi bērns")

    elif ievads >= 13 and ievads <= 19:
        print(f"Tavs vecums ir {ievads}, Tu esi tīnis")

    elif ievads >= 20:
        print(f"Tavs vecums ir {ievads}, Tu esi pieaugušais")
    