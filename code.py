import board
import busio
import usb_midi

# Initialize UART MIDI
uart = busio.UART(board.GP0, board.GP1, baudrate=31250)

# Initialize USB MIDI output
midi_out = usb_midi.ports[1]

# Initialize USB MIDI input
midi_in = usb_midi.ports[0]

while True:
    try:
        if uart.in_waiting > 0:
            # Send received MIDI message from UART to computer via USB MIDI
            midi_out.write(uart.read(uart.in_waiting))
            
        msg = midi_in.read()
        
        if msg:
            # Send received MIDI message from USB MIDI to external device via UART
            uart.write(msg)

    except Exception as e:
        print("An error occurred:", e)
