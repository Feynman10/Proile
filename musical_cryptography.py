import mido
from mido import Message, MidiFile, MidiTrack

# Define a mapping from letters to MIDI note numbers
note_mapping = {char: 60 + i for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')}

def text_to_notes(text):
    return [note_mapping[char] for char in text.upper() if char in note_mapping]

def create_midi(notes, filename):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    for note in notes:
        track.append(Message('note_on', note=note, velocity=64, time=32))
        track.append(Message('note_off', note=note, velocity=64, time=32))

    mid.save(filename)

message = "Hallå FRA."
notes = text_to_notes(message)
create_midi(notes, 'output.mid')
