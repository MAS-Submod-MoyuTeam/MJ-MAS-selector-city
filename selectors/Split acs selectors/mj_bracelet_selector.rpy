# Credit to RaVen for a template, submod by MayJay

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["bracelet_acs"] = {
        "_ev": "mj_bracelet_acs_select",
        "_min-items": 1,
        "change": "你能换一下你的手镯吗?",
        "wear": "你能戴个手镯吗?",
    }



#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_bracelet_acs_select",
            category=["外观"],
            prompt=store.mas_selspr.get_prompt("bracelet_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_bracelet_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="bracelet_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("你想让我戴什么样的手镯?")
        sel_map = {}

    m 1eua "好的 [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "噢，好吧."