
particle_to_id = {
  "onset": {
    "ㄱ": 0,
    "ㄲ": 1,
    "ㄴ": 2,
    "ㄷ": 3,
    "ㄸ": 4,
    "ㄹ": 5,
    "ㅁ": 6,
    "ㅂ": 7,
    "ㅃ": 8,
    "ㅅ": 9,
    "ㅆ": 10,
    "ㅇ": 11,
    "ㅈ": 12,
    "ㅉ": 13,
    "ㅊ": 14,
    "ㅋ": 15,
    "ㅌ": 16,
    "ㅍ": 17,
    "ㅎ": 18,
  },
  "nucleus": {
    "ￂ": 0,
    "ￃ": 1,
    "ￄ": 2,
    "ￅ": 3,
    "ￆ": 4,
    "ￇ": 5,
    "ￊ": 6,
    "ￋ": 7,
    "ￌ": 8,
    "ￍ": 9,
    "ￎ": 10,
    "ￏ": 11,
    "ￒ": 12,
    "ￓ": 13,
    "ￔ": 14,
    "ￕ": 15,
    "ￖ": 16,
    "ￗ": 17,
    "ￚ": 18,
    "ￛ": 19,
    "ￜ": 20,
  },
  "coda": {
    "∅": 0,
    "ﾡ": 1,
    "ﾢ": 2,
    "ﾣ": 3,
    "ﾤ": 4,
    "ﾥ": 5,
    "ﾦ": 6,
    "ﾧ": 7,
    "ﾩ": 8,
    "ﾪ": 9,
    "ﾫ": 10,
    "ﾬ": 11,
    "ﾭ": 12,
    "ﾮ": 13,
    "ﾯ": 14,
    "ﾰ": 15,
    "ﾱ": 16,
    "ﾲ": 17,
    "ﾴ": 18,
    "ﾵ": 19,
    "ﾶ": 20,
    "ﾷ": 21,
    "ﾸ": 22,
    "ﾺ": 23,
    "ﾻ": 24,
    "ﾼ": 25,
    "ﾽ": 26,
    "ﾾ": 27,
  },
}

id_to_particle = {
  "onset": {v: k for k, v in particle_to_id["onset"].items()},
  "nucleus": {v: k for k, v in particle_to_id["nucleus"].items()},
  "coda": {v: k for k, v in particle_to_id["coda"].items()},
}

def split_particle(text: str) -> list[tuple[str]]:
  result = []
  for syllable in text:
    ucode = ord(syllable)
    if 0xAC00 <= ucode <= 0xD7A3:
      kcode = ucode - 0xAC00
      onset = id_to_particle['onset'][kcode//588]
      nucleus = id_to_particle['nucleus'][kcode%588//28]
      coda = id_to_particle['coda'][kcode%588%28]
      result.append((onset, nucleus, coda))
    else:
      result.append((syllable,))
  return result

def combine(splitted_text: list[tuple[str]]) -> str:
  result = ''
  for syllable in splitted_text:
    if isinstance(syllable, tuple):
      if len(syllable) == 3:
        onset = particle_to_id['onset'][syllable[0]]
        nucleus = particle_to_id['nucleus'][syllable[1]]
        coda = particle_to_id['coda'][syllable[2]]
        ucode = 0xAC00 + (onset * 588) + (nucleus * 28) + coda
        result += chr(ucode)
      else:
        result += syllable[0]
    elif isinstance(syllable, str):
      result += syllable
    else:
      raise ValueError("Invalid syllable format")
  return result

def find_onset(onsets: str, target_text: str) -> int:
  onset_of_target_text = ''.join([x[0] for x in split_particle(target_text)])
  print(onset_of_target_text)
  return onset_of_target_text.find(onsets)