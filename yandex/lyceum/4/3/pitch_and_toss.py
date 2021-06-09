import struct
import wave


def pitch_and_toss():
    source = wave.open("in.wav", "rb")
    dest = wave.open("out.wav", "wb")

    dest.setparams(source.getparams())
    frames_count = source.getnframes()

    data = struct.unpack(
        "<" + str(frames_count) + "h",
        source.readframes(frames_count),
    )

    n = frames_count // 4
    a, b, c, d = (
        data[i * n: (frames_count if i == 3 else (i + 1) * n)]
        for i in range(4)
    )

    newframes = struct.pack("<" + str(frames_count) + "h", *(c + d + a + b))
    dest.writeframes(newframes)
    source.close()
    dest.close()


pitch_and_toss()
