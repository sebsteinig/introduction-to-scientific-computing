
  STRATEGI®

  Notes on the Supply of Ordnance Survey Digital Data 
  ---------------------------------------------------
  Directory Structure of the media
  --------------------------------

 
   This information is made up of 4 sections, containing examples:

   SECTION ONE - HIGH LEVEL STRUCTURE EXAMPLE
   SECTION TWO - AN EXAMPLE OF AN ORDER
   SECTION THREE - DIRECTORY STRUCTURE EXAMPLES
     

   ***********
   SECTION ONE   
   ***********

   SECTION ONE - HIGH LEVEL STRUCTURE EXAMPLE


   The directory structure of the media is shown below:


                                           ROOT 
                                            |
                ------------------------------------------------------
               |                |                  |                 |
              doc           gazetteer            data        Strategi_Readme.txt


   

   The high level structure will be explained further in Section 3.


   ***********
   SECTION TWO   
   ***********

   2a - EXAMPLE - GB - IN SHAPE, DXF and TAB
   2b - EXAMPLE - ORDER NOTES
   

   2a  EXAMPLE - GB - IN SHAPE, DXF and TAB
   -----------------------------------------------------------

 ROOT
   |
   |--doc
   |   |--Strategi_Area.txt
   |   |--Strategi_Release_YYYY_Change.txt
   |   |--StrategiSymbols.ttf (new True Type Font file)
   |   |--Styling_Guide.pdf
   | 
   |-- gazetteer
   |      |--Strategi_gazetteer_YYYY.txt      
   |
   |-- data
   |   |--dxf
   |   |   |
   |   |   |--gb_north
   |   |   |    |...(.dxf files)
   |   |   |--gb_south
   |   |        |...(.dxf files)
   |   |
   |   |--shapefile
   |   |   | 
   |   |   |--info
   |   |   |    |--...(.dat, .nit, .dir files)
   |   |   |--general_text*														
   |   |   |    |--...(.adf, .tat, .txt, .txx files)	
   |   |   |--transport_txt*
   |   |   |    |--...(.adf, .tat, .txt, .txx files)		
   |   |	|--...(.prj, .dbf, .shp, .shx, .lyr files)
   |   |
   |   |
   |   |--tab
   |        | 
   |        |...( .dat,.id .map .tab files)
   |            
   |           	     													
   |         
   |--Strategi_Readme.txt

Where * is the coverage file to cartographically display text. This looks like a folder in Windows Explorer but is described as a
coverage file when viewed in ESRI ArcMap.

   2b  EXAMPLE - ORDER NOTES
   -------------------------
   AREA/COVERAGE (GB),
   TRANSFER FORMAT (for example: AutoCAD® (Release 12) DXF™ format
                                 ESRI® Spatial data format
                                 MapInfo® proprietary format)
                                 MIDMIF Interchange format


   *************
   SECTION THREE  
   *************

   3a - ROOT directory
   3b - doc directory
   3c - gazetteer directory
   3d - data(based upon example in 2a and 2b) directory


   GB Data available as given in Section Two. The information reflects the GB filing structure; as per the example in the 
   Technical Specification section of the product User Guide.


   3a  ROOT directory
   ------------------
   The ROOT directory will contain the following directories:
    	data
	doc
   	gazetteer
   	
   The ROOT directory will also contain the following ASCII text file:
    	This file - Strategi_Readme.txt

   
   3b  doc directory
   -----------------

   Below are the types of documents contained within the doc directory. Additional information is
   also found within the Product Pages for Strategi on the Ordnance Survey Website:

   Strategi_Release_YYYY_Change.txt - Product changes associated with that release.
   Strategi_Area.txt - Information relating to geographical area.
   StrategiSymbols.ttf - the fonts for styling.
   Styling_Guide.pdf - a guide to using and amending the styling.

   The doc directory may contain additional documentation specific to that supply.
   Where YYYY refers to the year.


   3c  gazetteer directory
   -----------------------
   
   The data is National Coverage in an ASCII text format. The structure will appear as follows:

   ROOT
    |
    |-- gazetteer
        |
        |--Strategi_gazetteer_YYYY.txt

  

   3d  data directory
   ------------------
   The data directory will contain directories relating to the format you have ordered.
   The title of the sub-directory will be the name of your format. For example, if you have ordered
   DXF and SHAPE for GB, the structure will appear as follows:

    ROOT
     |
     |-- data
         |--dxf
         |        |--gb_north
         |        |     |...( .dxf files)
         |        |--gb_south
         |              |...( .dxf files)
         |--shapefile
         |        |--info
         |        |    |--...( dat .nit .dir files)
         |        |--general_text*														
         |        |    |--...(.adf .tat .txt .txx files)	
         |        |--transport_txt*
         |        |    |--...(.adf .tat .txt .txx files)		
         | 	  |--...(.prj .dbf .shp .shx, .lyr files)
    
   
   The data directory will contain the data files for your order, which may be split into further 
   sub-directories, depending upon the format ordered (for example, SHAPE).

   
   
  
   --------------------------------------------------------------------------------------------------
   README FILE CREATED BY ORDNANCE SURVEY, © January 2016
   --------------------------------------------------------------------------------------------------
   V1.0
