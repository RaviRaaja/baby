#!/usr/bin/env python
#
# BABY Framework Header module
# Created By D@nt3 (Ritik Dubey)
# Email : blackdeath8765@Gmail.Com

import random
def main_header():
	header_1 = r"""
    @@@    @@@  @@@  @   @
    @  @  @   @ @  @  @ @
    @@@@  @@@@@ @@@@   @
    @  @  @   @ @  @   @
    @@@   @   @ @@@    @


"""

	header_2 = r"""
    @##    @@@  @@@  @   @
    @  @  @   @ @  @  @ @
    @##@  @###@ @##@   @
    @  @  @   @ @  @   @
    @##   @   @ @@@    @
"""	
	header_3 = r"""
    @@@    @@@  @@@  @   @
    @  @  @   @ @  @  @ @
    @))@  @)))@ @))@   )
    @  @  @   @ @  @   @
    @@@   @   @ @@@    @
"""



	header_4 = r"""
    @@@    @@@  @@@  @   @
    @  @  @   @ @  @  @ @
    @@@@  @@@@@ @@@@   @
    @  @  @   @ @  @   @
    @@@   @   @ @@@    @
                                                                """
                                                                
	header_5 = r"""
                                          ^
                                      ^^^
                                     / ^^^
            ()     @@@@@   @@@@@     )       
           (D)     )    (  )    (   ( )      _       _
      ____( @(___  (    ) (     )   ) )      \\     // _______
     |____  N ___|(#)@@@   )@@@@(   ( )       \\   // |_______>
          ( T(     )    @ (     )   )@@@@@)    \\_//
           (3)    (     @  )   (   ( 0  0  )    \_/
            ()     )@@@@  (     )  ) 0000 )      @
                                  (  +++         @
                                   ^         <*@)
                                         ^ @@@@
                                          ^

  """
 
	hdr_num = random.randint(1, 5)
	if hdr_num ==1:
		print header_1
	if hdr_num ==2:
		print header_2
	if hdr_num ==3:
		print header_3
	if hdr_num ==4:
		print header_4
	if hdr_num ==5:
		print header_5


	
