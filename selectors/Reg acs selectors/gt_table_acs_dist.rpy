#creds to u/geneTechnician for these ones, thank you for allowing me to host them on github!

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["ltable_acs"] = {
        "_ev": "gt_ltable_acs_select",
        "_min-items": 1,
        "change": "你能在你的桌子左边放点别的东西吗?",
        "wear": "你能在你的桌子左边放点东西吗?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_ltable_acs_select",
            category=["桌面"],
            prompt=store.mas_selspr.get_prompt("ltable_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_ltable_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="ltable_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("你想让我把什么放在我的桌子上?")
        sel_map = {}

    m 1eua "好的 [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "哦, 好吧."
return


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["rtable_acs"] = {
        "_ev": "gt_rtable_acs_select",
        "_min-items": 1,
        "change": "你能把别的东西放在桌子的右边吗?",
        "wear": "你能把什么东西放在桌子的右边吗?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_rtable_acs_select",
            category=["桌面"],
            prompt=store.mas_selspr.get_prompt("rtable_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_rtable_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="rtable_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("你想让我把什么放在我的桌子上?")
        sel_map = {}

    m 1eua "好的 [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "哦, 好吧."
return


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["flowers_acs"] = {
        "_ev": "gt_flowers_acs_select",
        "_min-items": 1,
        "change": "你可以换一朵花吗?",
        "wear": "你可以在桌子上放一朵花吗?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_flowers_acs_select",
            category=["桌面"],
            prompt=store.mas_selspr.get_prompt("flowers_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_flowers_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="flowers_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("你想让我换什么花呢?")
        sel_map = {}

    m 1eua "好的 [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "哦, 好吧."
return