import os, subprocess, re;





while(True):

    comando = "pactl list sinks | grep 'Volume'"
    actual = subprocess.run(comando, shell=True, capture_output=True, text=True).stdout
    actual = re.findall(r"Volume:.*?(\d{1,3})%", actual);
    actual = int(actual[0]);
   
    os.system("clear");    

    print("""
                                    ───▄▀▌─▄▄▄▄
                                ──▄█▀──▌─▌─▌─▄▄▄▄
                                ▄▀─█▄──▌─▌─▌─▌─▌─▌
                                █─▀█─▌█▌█▌█▌─▌─▌─▌
                                ▀█▄█▀───────█▌█▌█▌
                              
            """)
   
    print(f"Volumen Actual: {actual}%")

    print("1. Subir volumen");
    print("2. Bajar volumen\n");
    

    try:
        volumen = int(input("Opcion: "));
    except Exception as e:
        print(f"Ha sucedido un error, no ingresaste bien: {e}")
            

    if(volumen == 1):
        os.system("pactl set-sink-volume @DEFAULT_SINK@ +10%")
    elif(volumen == 2):
        os.system("pactl set-sink-volume @DEFAULT_SINK@ -10%")

    








