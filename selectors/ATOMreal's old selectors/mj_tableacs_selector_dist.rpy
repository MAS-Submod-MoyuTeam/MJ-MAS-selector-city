# Special thanks to RaVen for a template
#Edited by ATOM (u/The_Foothills). You will never be able to completely get rid of my trace i left in the community
#the comment above me is an overdramatic lil bitch. get bent, atom. -u/mayday-mayjay


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["table_acs"] = {
        "_ev": "mj_table_acs_select",
        "_min-items": 1,
        "change": "你能放点别的东西在桌子上吗?",
        "wear": "你能放点东西在桌子上吗?",
    }

#keeping this here incase MAS devs ever try bring the need for this back
#init -9 python in mas_selspr:
    #GRP_TOPIC_LIST.append("table_acs")


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_table_acs_select",
            category=["桌子"],
            prompt=store.mas_selspr.get_prompt("table_acs", "改变"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_table_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="table_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("你想让我在桌子上放什么?")
        sel_map = {}

    m 1eua "好的 [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "哦，好吧."