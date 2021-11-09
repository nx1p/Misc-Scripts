########################################
#                                      #
#  Automated-individual-Archiver.ps1   #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: nx1p / Marceline Kuo-Arrigo  #
# Created: 10/11/2021                  #
# Last update: 10/11/2021              #
# Version: v1                          #
#                                      #
########################################
## TODOs / Features & Functions:
## ==============================
# - [X] Preform purpose, automatically iterate over subitems in a folder and archive them
# - [ ] Validation
#   - [ ] Validate $SrcFolder exists before contuining
#   - [ ] Validate successful archive processed
# - [ ] Error handling
#   - [ ] Throw useful errors e.g. if adding a subitem to an archive failed for some reason and exit
## ------------------------------
## Purpose:
## ===========
# Automated archiving of files
## ------------------------------
## Arguments:
## ===========
# Src - Folder with subitems that need to be individually archived
## ------------------------------
## ------------------------------

## Why:
## ===========
# Planning to off-load files on my archive HDD to Google Drive
# However, uploading large files using Rclone is problematic,
# There's no way to resume file uploading,
# So if an upload of a 50GB file is interrupted, 
# it has to be started from the beginning again.
#
# So I use 7zip to split the files into 1GB chunks, and while I'm at it,
# Compress the files as much as I can without sacrificing speed,
# Since usually the bottleneck in this process I'v found,
# is more the read speed of the HDD, not the CPU compression speed.
#
#
# And I want to individually archive files/folders,
# So to redownload and decompress them,
# I don't have to download a monolith of a 3TB archive, lol 
# Hence the scripting

## Misc notes:
## ===========
# Would've much preferred to do this scripting in Bash quite honestly.
# But after some quick research file system performance in WSL2,
# is quite terrible and well, 
# I gotta get more familar with Powershell sometime so, 
# Here we go!

param ($SrcFolder)

function Add-Archive {
    # Add-Archive
    # =============
    # Adds folder/file(s) to target archive,
    # Automatically splits archives up into 2GB chunks,
    # Calls 7z-zstd to do this (Is that bad Powershell-ness?).
    #
    # Parameters:
    # <Src> - Source folder/files
    # <Dst> - Destination archive(s)

    [CmdletBinding()]
	param(
		[Parameter()]
		[string] $Src,
        [string] $Dst
	)
    

    & "C:\Program Files\7-Zip-Zstandard\7za" a $Dst -m0=LIZARD -mx43 -v1G $Src

}



# problem solving steps
# 1. take target folder of subitems
# 2. iterate thru subitems
# 3. for each sub item, 
#   3a. add to archive, so src will be the subitem, 
#       the dst will be 
#            current working directory 
#          + the folder structure of path to subitem 
#          + folder for subitem archive files?
#          + plus subitem name
#          + ".7z"?
#       so.. calculate all these values for dst.. oki, cool.

Get-ChildItem $SrcFolder | 
Foreach-Object {

    [String]$CurrentDirectory = $(Get-Location)
    [String]$FolderStructure = $($_.Parent -replace '^..','')
    [String]$SubItemName = $_.Name

    #Write-Host $CurrentDirectory
    #Write-Host $FolderStructure
    #Write-host $SubItemName
    

    $ArchiveDst = 
        $CurrentDirectory  + 
        $FolderStructure   + 
        "\" + $SubItemName +
        "\$SubItemName.7z"
    
    #Write-Host $ArchiveDst
    #Write-Host ""


    Add-Archive -Src $_.FullName -Dst $ArchiveDst
}