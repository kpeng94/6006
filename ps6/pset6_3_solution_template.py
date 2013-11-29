# This solution template should be turned in through our submission site, at
# https://alg.csail.mit.edu

######################################################################################
### WARNING:                                                                       ###
### Be sure to write the Python code yourself!  We do run sophisticated automated  ###
### comparisons between each pair of programs turned in.  We are saddened and      ###
### troubled each year when a few studentsturn in nearly identical programs, and   ###
### we have to administer appropriate consequences.  It is better to turn in a     ###
### statement that you didn't have time to complete the assignment than to turn in ###
### the same code as someone else.                                                 ###
######################################################################################

debug_boxes = False

# Core14_AFMs/Times-Roman.py
charwidth = {
  '0': 6,
  '1': 6,
  '2': 6,
  '3': 6,
  '4': 6,
  '5': 6,
  '6': 6,
  '7': 6,
  '8': 6,
  '9': 6,
  'a': 5.3280000000000003,
  'b': 6,
  'c': 5.3280000000000003,
  'd': 6,
  'e': 5.3280000000000003,
  'f': 3.9960000000000004,
  'g': 6,
  'h': 6,
  'i': 3.3360000000000003,
  'j': 3.3360000000000003,
  'k': 6,
  'l': 3.3360000000000003,
  'm': 9.3360000000000003,
  'n': 6,
  'o': 6,
  'p': 6,
  'q': 6,
  'r': 3.9960000000000004,
  's': 4.6680000000000001,
  't': 3.3360000000000003,
  'u': 6,
  'v': 6,
  'w': 8.6639999999999997,
  'x': 6,
  'y': 6,
  'z': 5.3280000000000003,
  'A': 8.6639999999999997,
  'B': 8.0040000000000013,
  'C': 8.0040000000000013,
  'D': 8.6639999999999997,
  'E': 7.3319999999999999,
  'F': 6.6720000000000006,
  'G': 8.6639999999999997,
  'H': 8.6639999999999997,
  'I': 3.9960000000000004,
  'J': 4.6680000000000001,
  'K': 8.6639999999999997,
  'L': 7.3319999999999999,
  'M': 10.667999999999999,
  'N': 8.6639999999999997,
  'O': 8.6639999999999997,
  'P': 6.6720000000000006,
  'Q': 8.6639999999999997,
  'R': 8.0040000000000013,
  'S': 6.6720000000000006,
  'T': 7.3319999999999999,
  'U': 8.6639999999999997,
  'V': 8.6639999999999997,
  'W': 11.327999999999999,
  'X': 8.6639999999999997,
  'Y': 8.6639999999999997,
  'Z': 7.3319999999999999,
  '!': 3.9960000000000004,
  '"': 4.8959999999999999,
  '#': 6,
  '$': 6,
  '%': 9.9959999999999987,
  '&': 9.3360000000000003,
  "'": 3.9960000000000004,
  '(': 3.9960000000000004,
  ')': 3.9960000000000004,
  '*': 6,
  '+': 6.7679999999999989,
  ',': 3,
  '-': 3.9960000000000004,
  '.': 3,
  '/': 3.3360000000000003,
  ':': 3.3360000000000003,
  ';': 3.3360000000000003,
  '<': 6.7679999999999989,
  '=': 6.7679999999999989,
  '>': 6.7679999999999989,
  '?': 5.3280000000000003,
  '@': 11.052,
  '[': 3.9960000000000004,
  '\\': 3.3360000000000003,
  ']': 3.9960000000000004,
  '^': 5.6280000000000001,
  '_': 6,
  '`': 3.9960000000000004,
  '{': 5.7599999999999998,
  '|': 2.4000000000000004,
  '}': 5.7599999999999998,
  '~': 6.4920000000000009,
  ' ': 3,
}
kerning = {
  ('a','v'): -0.23999999999999999,
  ('a','w'): -0.17999999999999999,
  ('b','u'): -0.23999999999999999,
  ('b','v'): -0.17999999999999999,
  ('b','.'): -0.47999999999999998,
  ('c','y'): -0.17999999999999999,
  ('e','g'): -0.17999999999999999,
  ('e','v'): -0.30000000000000004,
  ('e','w'): -0.30000000000000004,
  ('e','x'): -0.17999999999999999,
  ('e','y'): -0.17999999999999999,
  ('f','a'): -0.12,
  ('f','f'): -0.30000000000000004,
  ('f','i'): -0.23999999999999999,
  ('f',"'"): 0.66000000000000003,
  ('g','a'): -0.059999999999999998,
  ('h','y'): -0.059999999999999998,
  ('i','v'): -0.30000000000000004,
  ('k','e'): -0.12,
  ('k','o'): -0.12,
  ('k','y'): -0.17999999999999999,
  ('l','w'): -0.12,
  ('n','v'): -0.47999999999999998,
  ('n','y'): -0.17999999999999999,
  ('o','v'): -0.17999999999999999,
  ('o','w'): -0.30000000000000004,
  ('o','y'): -0.12,
  ('p','y'): -0.12,
  ('r','g'): -0.21599999999999997,
  ('r',','): -0.47999999999999998,
  ('r','-'): -0.23999999999999999,
  ('r','.'): -0.66000000000000003,
  ('v','a'): -0.30000000000000004,
  ('v','e'): -0.17999999999999999,
  ('v','o'): -0.23999999999999999,
  ('v',','): -0.78000000000000003,
  ('v','.'): -0.78000000000000003,
  ('w','a'): -0.12,
  ('w','o'): -0.12,
  ('w',','): -0.78000000000000003,
  ('w','.'): -0.78000000000000003,
  ('x','e'): -0.17999999999999999,
  ('y',','): -0.78000000000000003,
  ('y','.'): -0.78000000000000003,
  ('A','v'): -0.8879999999999999,
  ('A','w'): -1.1040000000000001,
  ('A','y'): -1.1040000000000001,
  ('A','C'): -0.47999999999999998,
  ('A','G'): -0.47999999999999998,
  ('A','O'): -0.66000000000000003,
  ('A','Q'): -0.66000000000000003,
  ('A','T'): -1.3320000000000001,
  ('A','U'): -0.66000000000000003,
  ('A','V'): -1.6200000000000001,
  ('A','W'): -1.0800000000000001,
  ('A','Y'): -1.26,
  ('A',"'"): -1.3320000000000001,
  ('B','A'): -0.42000000000000004,
  ('B','U'): -0.12,
  ('D','A'): -0.47999999999999998,
  ('D','V'): -0.47999999999999998,
  ('D','W'): -0.35999999999999999,
  ('D','Y'): -0.66000000000000003,
  ('F','a'): -0.17999999999999999,
  ('F','o'): -0.17999999999999999,
  ('F','A'): -0.8879999999999999,
  ('F',','): -0.95999999999999996,
  ('F','.'): -0.95999999999999996,
  ('J','A'): -0.71999999999999997,
  ('K','e'): -0.30000000000000004,
  ('K','o'): -0.42000000000000004,
  ('K','u'): -0.17999999999999999,
  ('K','y'): -0.30000000000000004,
  ('K','O'): -0.35999999999999999,
  ('L','y'): -0.66000000000000003,
  ('L','T'): -1.1040000000000001,
  ('L','V'): -1.2000000000000002,
  ('L','W'): -0.8879999999999999,
  ('L','Y'): -1.2000000000000002,
  ('L',"'"): -1.1040000000000001,
  ('N','A'): -0.42000000000000004,
  ('O','A'): -0.42000000000000004,
  ('O','T'): -0.47999999999999998,
  ('O','V'): -0.60000000000000009,
  ('O','W'): -0.42000000000000004,
  ('O','X'): -0.47999999999999998,
  ('O','Y'): -0.60000000000000009,
  ('P','a'): -0.17999999999999999,
  ('P','A'): -1.1040000000000001,
  ('P',','): -1.3320000000000001,
  ('P','.'): -1.3320000000000001,
  ('Q','U'): -0.12,
  ('R','O'): -0.47999999999999998,
  ('R','T'): -0.71999999999999997,
  ('R','U'): -0.47999999999999998,
  ('R','V'): -0.95999999999999996,
  ('R','W'): -0.66000000000000003,
  ('R','Y'): -0.78000000000000003,
  ('T','a'): -0.95999999999999996,
  ('T','e'): -0.84000000000000008,
  ('T','i'): -0.42000000000000004,
  ('T','o'): -0.95999999999999996,
  ('T','r'): -0.42000000000000004,
  ('T','u'): -0.54000000000000004,
  ('T','w'): -0.95999999999999996,
  ('T','y'): -0.95999999999999996,
  ('T','A'): -1.1160000000000001,
  ('T','O'): -0.21599999999999997,
  ('T',','): -0.8879999999999999,
  ('T','-'): -1.1040000000000001,
  ('T','.'): -0.8879999999999999,
  ('T',':'): -0.60000000000000009,
  ('T',';'): -0.66000000000000003,
  ('U','A'): -0.47999999999999998,
  ('V','a'): -1.3320000000000001,
  ('V','e'): -1.3320000000000001,
  ('V','i'): -0.71999999999999997,
  ('V','o'): -1.548,
  ('V','u'): -0.89999999999999991,
  ('V','A'): -1.6200000000000001,
  ('V','G'): -0.17999999999999999,
  ('V','O'): -0.47999999999999998,
  ('V',','): -1.548,
  ('V','-'): -1.2000000000000002,
  ('V','.'): -1.548,
  ('V',':'): -0.8879999999999999,
  ('V',';'): -0.8879999999999999,
  ('W','a'): -0.95999999999999996,
  ('W','e'): -0.95999999999999996,
  ('W','i'): -0.47999999999999998,
  ('W','o'): -0.95999999999999996,
  ('W','u'): -0.60000000000000009,
  ('W','y'): -0.87599999999999989,
  ('W','A'): -1.4399999999999999,
  ('W','O'): -0.12,
  ('W',','): -1.1040000000000001,
  ('W','-'): -0.78000000000000003,
  ('W','.'): -1.1040000000000001,
  ('W',':'): -0.44399999999999995,
  ('W',';'): -0.44399999999999995,
  ('Y','a'): -1.2000000000000002,
  ('Y','e'): -1.2000000000000002,
  ('Y','i'): -0.66000000000000003,
  ('Y','o'): -1.3200000000000001,
  ('Y','u'): -1.3320000000000001,
  ('Y','A'): -1.4399999999999999,
  ('Y','O'): -0.35999999999999999,
  ('Y',','): -1.548,
  ('Y','-'): -1.3320000000000001,
  ('Y','.'): -1.548,
  ('Y',':'): -1.1040000000000001,
  ('Y',';'): -1.1040000000000001,
  ("'",'d'): -0.60000000000000009,
  ("'",'l'): -0.12,
  ("'",'r'): -0.60000000000000009,
  ("'",'s'): -0.66000000000000003,
  ("'",'t'): -0.21599999999999997,
  ("'",'v'): -0.60000000000000009,
  ("'","'"): -0.8879999999999999,
  ("'",' '): -0.8879999999999999,
  (',',"'"): -0.84000000000000008,
  ('.',"'"): -0.84000000000000008,
  ('`','A'): -0.95999999999999996,
  ('`','`'): -0.8879999999999999,
  (' ','A'): -0.66000000000000003,
  (' ','T'): -0.21599999999999997,
  (' ','V'): -0.60000000000000009,
  (' ','W'): -0.35999999999999999,
  (' ','Y'): -1.0800000000000001,
}

def width (word):
  return sum (charwidth[char] for char in word)

def minwidth (line):
  line = list (line)
  return 3 * (len (line) - 1) + sum (width (word) for word in line)

class PDF:
  """PDF writer.  A canvas for words that can be written to a PDF file.

  Write all your words at specified coordinates, using the
  pdf.write(x, y, word) method.  Then save your file using the
  pdf.save(filename) method, or get it as a string using str(pdf).
  Sample usage::

      pdf = PDF()
      pdf.write (50, 50, 'hello')
      pdf.save ('test.pdf')
  """
  def __init__ (self):
    self._words = []
  def write (self, x, y, word):
    """Write the given word at the given (x, y) coordinates."""
    self._words.append ((x, y, word))
  def save (self, filename):
    """Save all written words as a PDF file with given filename."""
    f = open (filename, 'wb')
    f.write (str (self))
    f.close ()
  def __str__ (self):
    """Return the entire PDF file as a string."""
    self._pos = 0
    self._data = ''
    self._objects = [None]
    self._write ('%PDF-1.4\n')
    self._writeobj ('''\
1 0 obj
  << /Type /Catalog
     /Pages 2 0 R
  >>
endobj
''')
    self._writeobj ('''\
2 0 obj
  << /Type /Pages
     /Kids [ 3 0 R
           ]
     /Count 1
  >>
endobj
''')
    self._writeobj ('''\
3 0 obj
  << /Type /Page
     /Parent 2 0 R
     /MediaBox [0 0 612 792]
     /Resources
       << /Font
            << /F1 4 0 R >>
       >>
     /Contents 5 0 R
  >>
endobj
''')
    self._writeobj ('''\
4 0 obj
  << /Type /Font
     /Subtype /Type1
     /BaseFont /Times-Roman
  >>
endobj
''')

    commands = ['  72 72 468 648 re S']
    for x, y, word in self._words:
      x += 72                 ## 1-inch margin
      y = 792 - 72 - y        ## 1-inch margin, and start at the top
      ## Grey bounding boxes for debugging:
      if debug_boxes:
        commands.append ('  %.17g %.17g %.17g %.17g re 0.8 g f' %
          (x, y, width (word), 12))
      commands.append ('''\
  BT
    /F1 12 Tf
    %.17g %.17g Td
    0 g
    (%s) Tj
  ET
''' % (x, y, word.replace ('\\', '\\\\').replace ('(', '\\(')
                 .replace (')', '\\)').replace ('\n', '\\n')
                 .replace ('\r', '\\r').replace ('\t', '\\t')
                 .replace ('\b', '\\b').replace ('\f', '\\f')))
    commands = '\n'.join (commands)

    self._writeobj ('''\
5 0 obj
  << /Length %d >>
stream
%s
endstream
endobj
''' % (len (commands) + commands.count ('\n'), commands))
    xrefpos = self._pos
    self._write ('''\
xref
0 %d
0000000000 65535 f
''' % len (self._objects))
    for x in self._objects[1:]:
      self._write ('%010d 00000 n\n' % x)
    self._write ('''\
trailer
  << /Size %d
     /Root 1 0 R
  >>
startxref
%d
%%%%EOF
''' % (len (self._objects), xrefpos))
    return self._data
  def _write (self, line):
    line = line.replace ('\n', '\r\n')
    self._data += line
    self._pos += len (line)
  def _writeobj (self, obj):
    self._objects.append (self._pos)
    self._write (obj)

#####################
###  Problem 6-3  ###
#####################

### Sample Inputs ###
#case1 = "Two households, both alike in dignity, in fair Verona, where we lay our scene, from ancient grudge break to new mutiny, where civil blood makes civil hands unclean. From forth the fatal loins of these two foes a pair of star-cross'd lovers take their life; whole misadventured piteous overthrows do with their death bury their parents' strife. The fearful passage of their death-mark'd love, and the continuance of their parents' rage, which, but their children's end, nought could remove, is now the two hours' traffic of our stage; the which if you with patient ears attend, what here shall miss, our toil shall strive to mend."
#case2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In auctor pretium justo ac sodales. Vivamus fringilla, est sed gravida interdum, sapien est tempus enim, venenatis lobortis libero odio sed massa. Proin sem turpis, aliquam at mollis vitae, placerat at ante. Aliquam ante sapien, faucibus ac nisl vel, luctus venenatis mauris. Duis nisi dolor, rutrum eget ullamcorper a, tincidunt sed felis. In luctus, nulla sit amet vulputate venenatis, eros nunc suscipit nunc, quis tincidunt sapien sapien at justo. Donec condimentum ut est nec rutrum. Proin tellus nunc, euismod et est at, accumsan bibendum augue. Nulla in volutpat magna."
#case3 = "Mr Phileas Fogg lived, in 1872, at No. 7, Saville Row, Burlington Gardens, the house in which Sheridan died in 1814. He was one of the most noticeable members of the Reform Club, though he seemed always to avoid attracting attention; an enigmatical personage, about whom little was known, except that he was a polished man of the world. People said that he resembled Byron, - at least that his head was Byronic; but he was a bearded, tranquil Byron, who might live on a thousand years without growing old."

def layout(x):
    pass
