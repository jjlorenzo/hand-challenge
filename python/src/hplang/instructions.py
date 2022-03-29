import sys
from .memory import Buffer


def translate(instructions: str, progress=False) -> str:
  index = 0
  memory = Buffer()
  output = []
  while index < len(instructions):
    match instructions[index]:
      case "👉":
        memory.next()
        index += 1
      case "👈":
        memory.prev()
        index += 1
      case "👆":
        memory.inc()
        index += 1
      case "👇":
        memory.dec()
        index += 1
      case "🤜":
        if memory.cur == 0:
          jmp = 1
          idx = index + 1
          while jmp > 0 and (idx < len(instructions) - 1):
            match instructions[idx]:
              case "🤜":
                jmp += 1
              case "🤛":
                jmp -= 1
            if jmp != 0:
              idx += 1
          index = idx + 1
        else:
          index += 1
      case "🤛":
        if memory.cur != 0:
          jmp = 1
          idx = index - 1
          while jmp > 0 and (idx >= 0):
            match instructions[idx]:
              case "🤛":
                jmp += 1
              case "🤜":
                jmp -= 1
            if jmp != 0:
              idx -= 1
          index = idx + 1
        else:
          index += 1
      case "👊":
        output.append(chr(memory.cur))
        index += 1
        if progress:
          sys.stdout.write(chr(memory.cur))
          sys.stdout.flush()
      case _:
        index += 1
  return "".join(output)
