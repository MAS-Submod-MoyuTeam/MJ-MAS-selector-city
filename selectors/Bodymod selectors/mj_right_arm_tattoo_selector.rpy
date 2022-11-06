# Credit to RaVen / ATOMreal for a template, submod by mayday-mayjay (dont reupload my stuff, nerd)

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["rarmtattoo_acs"] = {
        "_ev": "mj_rarmtattoo_acs_select",
        "_min-items": 1,
        "change": "你能改变你右臂上的纹身吗?",
        "wear": "你能在右手臂上纹个纹身吗?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_rarmtattoo_acs_select",
            category=["外观"],
            prompt=store.mas_selspr.get_prompt("rarmtattoo_acs", "改变"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_rarmtattoo_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="rarmtattoo_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("你想让我纹什么?")
        sel_map = {}

    m 1eua "好的 [player]!"

    call mas_selector_sidebar_select_acs(use_acs, [mas_quipExp('6eua')], mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "噢，好吧."
