from pushbullet import Pushbullet

pb_key = 'o.8tkekkkOYX2n8yjp9yBgm3T20UWUd0W9'
pb = Pushbullet(pb_key)
pb.push_note("This is the title", "This is the body")
