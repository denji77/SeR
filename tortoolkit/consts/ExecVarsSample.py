try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "dfeaadec16aff49b3665ed2a9633c8cf"
        API_ID = 4512926
        
        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = "anime.touka.workers.dev/0:/"
        
        BOT_TOKEN = "1632896073:AAHxCFKuzKjAudZU_QiuU50eLb0mLJABBcA"
        BASE_URL_OF_BOT = "https://anime19.tk"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [-1001263450758, 804248372]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 2097152000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▓"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▒"

        # DB URI for access heroku prodrige url whatever 💁‍♀️
        DB_URI = "postgres://ovswmwwzgazcug:33e60ce493574ef4ef239968e2cc67b2d0dcdd5c1c3754ab219b0eeefc77f816@ec2-34-206-8-52.compute-1.amazonaws.com:5432/d519kf8mcf90aq"
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of the torrent allowed
        MAX_YTPLAYLIST_SIZE = 200
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 100

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = True
        




