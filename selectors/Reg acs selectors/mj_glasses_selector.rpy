# Credit to RaVen / ATOMreal for a template, submod by mayday-mayjay (dont reupload my stuff, nerd)

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["glasses_acs"] = {
        "_ev": "mj_glasses_acs_select",
        "_min-items": 1,
        "change": "你可以换一副眼镜吗?",
        "wear": "你可以戴一副眼镜吗?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_glasses_acs_select",
            category=["桌面"],
            prompt=store.mas_selspr.get_prompt("glasses_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_glasses_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="glasses_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("想让我戴哪副眼睛呢?")
        sel_map = {}

    m 1eua "好的 [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "哦, 好吧."
