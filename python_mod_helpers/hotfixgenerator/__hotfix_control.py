# I have to put the program like this because in order to make hotfixes in the way
# the bl3data/bl3hotfixmod work, it has to be executed in a row in order to work
from bl3hotfixmod import Mod
from _global_lists import Mod_Header, Reg_hotfix, Table_Hotfix, Mesh_Hotfix, Queue_Order, Comment_Queue, Headers_Queue
################################################################################################################################################################
#####################################################################################################################################################################################
def Create_HotFix_File():
    # All these are different indexes because they are all going to pull from different queues, and I need to kepp track of them indifidually.
    Queue_Index = 0 # This is a special one. one you add sometihng to a hotfix or call a new line, that command is added a queue list and thats how my program knows what order to go in when creating your hotfix
    Reg_Index = 0
    Table_Index = 0
    Mesh_Index = 0
    Comment_Index = 0
    Header_Index = 0
    # Create hotfix file from information
    # If you don't give it someting, this is what I will replace it with as the program needs to be able to call apon this file later to inset things into it
    # Also its a little bit of an easter egg
    if len(Mod_Header) < 6:
        Mod_Header.extend(["Chadd", "Chadd", "Chadd", "Chadd", "Chadd", "Chadd"])

    # We need this to be the first step, as the rest of the program depends on it
    File_Name, Mod_Title, Author_Name, Description, Version, Catagory = Mod_Header[0], Mod_Header[1], Mod_Header[2], Mod_Header[3], Mod_Header[4], Mod_Header[5]
    mod = Mod(File_Name + '.bl3hotfix', Mod_Title, Author_Name, [Description,], lic=Mod.CC_BY_SA_40, v=Version, cats=Catagory,) # Very important, as the rest of the porgram relies on this working as it writes to these filese

    """
    Things to add:
    header_lines
    """
    # Used to assign mod types, may change later if not working
    def patch_types(hold):
        if hold == 'Mod.PATCH': hold = Mod.PATCH
        elif hold == 'Mod.LEVEL': hold = Mod.LEVEL
        elif hold == 'Mod.EARLYLEVEL': hold = Mod.EARLYLEVEL
        elif hold == 'Mod.CHAR': hold = Mod.CHAR
        elif hold == 'Mod.PACKAGE': hold = Mod.PACKAGE
        elif hold == 'Mod.POST': hold = Mod.POST
        else: hold = Mod.PATCH
        return hold

    """
    The main and most important part of the code.
    What this will do is attempt to put the hotfixes inside of your desired code
    How I have this set up is that it will attempt to create a hotfix given the inputs inside of the file created.
    If something goes wrong in the creation process however, i do not want it to error out and cancel the rest if they are fine.
    The code will try and execute the creation of hotfixes, but if something bad happens then what this will try is to ignore that, then move the index up to what would be the next set would be
    Hopefully this will handle a lot of edge and error handling, and when creating a lot of hotfixes at once, it can be overwelming and mistakes are bound to happen
    """
    while Queue_Index < len(Queue_Order):
        if Queue_Order[Queue_Index] == "Regular hotfix":
            try:
                hf_type = Reg_hotfix[Reg_Index]
                hf_type = patch_types(hf_type)
                notification_flag = Reg_hotfix[Reg_Index+1]
                package = Reg_hotfix[Reg_Index+2]
                obj_name = Reg_hotfix[Reg_Index+3]
                attr_name = Reg_hotfix[Reg_Index+4]
                # prev_val_len = Reg_hotfix[regular_hotfix+5] # I do not know this was not needed when I was first coding this, but I want to keep it here just in case I someday do need it.
                prev_val = Reg_hotfix[Reg_Index+6]
                new_val = Reg_hotfix[Reg_Index+7]
                mod.reg_hotfix(hf_type, package, obj_name,attr_name, new_val, prev_val, notification_flag)
            except: print("Something went wrong") #Hopefully this prints out if the hotfix wents wrong and it will continue one like normal
            finally: Reg_Index += 8 #Once everything is done, this command will be ran and hopefully it works as i intended it

        # Table_Hotfix Mesh_Hotfix
        elif Queue_Order[Queue_Index] == "Table hotfixes":
            try:
                hf_type = Table_Hotfix[Table_Index]
                hf_type = patch_types(hf_type)
                notification_flag = Table_Hotfix[Table_Index+1]
                package = Table_Hotfix[Table_Index+2]
                obj_name = Table_Hotfix[Table_Index+3]
                row_name = Table_Hotfix[Table_Index+4]
                attr_name = Table_Hotfix[Table_Index+5]
                # prev_val_len = Table_Hotfix[table_hotfix_index+6]
                prev_val = Table_Hotfix[Table_Index+7]
                new_val = Table_Hotfix[Table_Index+8]
                mod.table_hotfix(hf_type, package, obj_name, row_name,attr_name, new_val, prev_val, notification_flag)
            except: print("Something went wrong")
            finally: Table_Index += 8

        elif Queue_Order[Queue_Index] == "Mesh hotfixes":
            try:
                hf_type = Mesh_Hotfix[Mesh_Index]
                hf_type = patch_types(hf_type)
                notification_flag = Mesh_Hotfix[Mesh_Index+1]
                map_path = Mesh_Hotfix[Mesh_Index+2]
                mesh_path = Mesh_Hotfix[Mesh_Index+3]
                # Since i have the user  enter numbers like: n,n,n, I need it to split up into a list so that the program can handle it easier
                location = str(Mesh_Hotfix[Mesh_Index+4]).split(",")
                rotation = str(Mesh_Hotfix[Mesh_Index+5]).split(",")
                scale = str(Mesh_Hotfix[Mesh_Index+6]).split(",")
                transparent = Mesh_Hotfix[Mesh_Index+7]
                mod.mesh_hotfix(map_path, mesh_path, (int(location[0]), int(location[1]), int(location[2])), (int(rotation[0]), int(rotation[1]), int(rotation[2])), (int(scale[0]), int(scale[1]), int(scale[2])), transparent, hf_type, notification_flag)
            except: print("Something went wrong")
            finally: Mesh_Index += 8

        elif Queue_Order[Queue_Index] == "New line":
            try: mod.newline
            except: print("Something went wrong")

        elif Queue_Order[Queue_Index] == "Comment":
            try: mod.comment(comment_str=Comment_Queue[Comment_Index]) # If the user wronte a comment, then it will be called here and it should move on to hte next one
            except: print("Something went wrong")
            finally: Comment_Index += 1

        # not yet implimented
        elif Queue_Order[Queue_Index] == "Header":
            try: mod.header_lines(Headers_Queue[Header_Index])
            except: print("Something went wrong")
            finally: Header_Index += 1
        Queue_Index += 1