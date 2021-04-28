import re
import time
import sys
from tqdm import tqdm
con_array = []
bad_array = []






fileObj = open("rockyou.txt", "r",encoding="utf8",errors="ignore") #opens the file in read mode
wdList_array = fileObj.read().splitlines() #puts the file into an array
fileObj.close()
for element in wdList_array:
        con_array.append(element.strip())

print("""                                                                                
                                 ***                                   
                            .,@@@@@@@@@@@%                              
                         ..@@@@@@@@@@@@@@@@@*.                          
                         @@@@@@@@@@@@@@@@@@@@@                          
                        @@@@@@@@@@@@@@@@@@@@@@@                         
                      .#@@@@@@@@@@@@@@@@@@@@@@@@,                       
                      *@@@@@@@@@@@@@@@@@@@@@@@@@                        
                      .#@@@@@@@@@@@@@@@@@@@@@@@@,                       
         ,.%&%, .       @@@@@@@@@@@@@@@@@@@@@@@        * #&%,           
      .(@@@@@@@@@@.      @@@@@(@@@@@@@@@@@@@@@      .@@@@@@@@@@@        
      @@@@ ( / @@@@@@.    /@ @@@.@@@@@ @@@ @@    . @@@@@%    *@@@@      
    .&@,.       ,%@@@@@. ,@@@/ @@@@@@@@@.(#@@@..@@@@@@         .@@      
      @           ,%@@@@@&(@@(((*/@@@&,##.@@@ @@@@@@           /@%      
                     %@@@(.@@@@@@@@@@@@@@@@@&.@@@@                      
    @@@@@@@@@@@@@@@@@@@{ Jen's PassWord Checker }@@@@@@@@@@@@@@@@@.    
 (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
  @@@#                 * .@@@@@@@@@@@@@@@@@@@# .                  @@@#  
 ,@@@%,               .&@@@@@@@ .@@@@@#.%@@@@@@@                  @@@.  
   @@@,             .@@@@@@@ ,  .@@@@@(   .&@@@@@@%.             (@@(.  
    *@@          .&@@@@@@        @@@@@/       @@@@@@@ .         &@@     
               .@@@@@@ *         @@@@@.         .@@@@@@                 
              .@@@@@            .@@@@@            *@@@@@                
               @@@@@             @@@@@            ,@@@@@                
                 @@@@&.         ,(@@@@*          ,@@@@*                 
                    @@@@@@*       @@@#       @@@@@@,*                   
                                  *@@@                                   
                                  .@%                                   
                                    .                                  
""")
for value in con_array:
    
        
      if (len(value)< 8):
          bad_array.append(value)
      elif value.islower() or value.isupper():
         bad_array.append(value)
      elif not re.search("[$#@]",value):
       bad_array.append(value)
for i in tqdm (range (len(con_array)), desc="Checking..."):
    pass

with tqdm(total=len(con_array), desc="Removing Bad Passwords...") as pbar:
   for x in con_array:
    for value in bad_array:
        con_array.remove(value)
        pbar.update(1)

          
  
with open('NotValidPassword.txt', 'w') as file_handler:
    with tqdm(total=len(bad_array), desc="Writing Bad Passwords...") as pbar:
        for item in bad_array:
            file_handler.write("{}\n".format(item))
            pbar.update(1) 