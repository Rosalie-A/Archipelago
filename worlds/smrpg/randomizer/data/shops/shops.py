from smrpgpatchbuilder.datatypes.shops.classes import Shop, ShopCollection
from ..items.items import *
from ..variables.shop_names import *


shops: list[Shop] = [None] * 33 # type: ignore
shops[SH00_MUSHROOM_KINGDOM] = Shop(
    index=0,
    items=[
        MushroomItem,
        HoneySyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        ShirtItem,
        PantsItem,
        JumpShoesItem,
        AntidotePinItem,
    ])
shops[SH01_ROSE_TOWN_ITEM] = Shop(
    index=1,
    items=[
        MushroomItem,
        HoneySyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
    ])
shops[SH02_ROSE_TOWN_ARMOR] = Shop(
    index=2,
    items=[
        ThickShirtItem,
        ThickPantsItem,
        JumpShoesItem,
        AntidotePinItem,
        WakeUpPinItem,
        TrueformPinItem,
        FearlessPinItem,
    ])
shops[SH03_FROG_DISCIPLE] = Shop(
    index=3,
    items=[
        SeeYaItem,
        EarlierTimesItem,
        ExpBoosterItem,
        CoinTrickItem,
        ScroogeRingItem,
    ],
    buy_frog_coin_one=True)
shops[SH04_MOLEVILLE] = Shop(
    index=4,
    items=[
        PunchGloveItem,
        FingerShotItem,
        CymbalsItem,
        MegaShirtItem,
        MegaCapeItem,
        MegaPantsItem,
        WorkPantsItem,
        MidMushroomItem,
        MapleSyrupItem,
    ])
shops[SH05_MARRYMORE] = Shop(
    index=5,
    items=[
        SuperHammerItem,
        HandGunItem,
        WhompGloveItem,
        ChompShellItem,
        HappyShirtItem,
        HappyPantsItem,
        HappyCapeItem,
        HappyShellItem,
        BtubRingItem,
        MidMushroomItem,
        MapleSyrupItem,
    ])
shops[SH06_FROG_COIN_EMPORIUM] = Shop(
    index=6,
    items=[
        SleepyBombItem,
        BracerItem,
        EnergizerItem,
        CrystallineItem,
        PowerBlastItem,
    ],
    buy_frog_coin=True)
shops[SH07_SEA_AND_SHIP_SHAMAN] = Shop(
    index=7,
    items=[
        HurlyGlovesItem,
        SuperHammerItem,
        HandGunItem,
        WhompGloveItem,
        SailorShirtItem,
        SailorPantsItem,
        SailorCapeItem,
        NauticaDressItem,
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])
shops[SH08_SEASIDE_TOWN_MINION] = Shop(
    index=8,
    items=[
        BadMushroomItem,
        MukuCookieItem,
        FrightBombItem,
        FireBombItem,
        IceBombItem,
    ])
shops[SH09_JUICE_BAR_BASE] = Shop(
    index=9,
    items=[
        FroggieDrinkItem,
    ])
shops[SH10_JUICE_BAR_ALTO] = Shop(
    index=10,
    items=[
        FroggieDrinkItem,
        ElixirItem,
    ],
    discount_12=True)
shops[SH11_JUICE_BAR_TENOR] = Shop(
    index=11,
    items=[
        FroggieDrinkItem,
        ElixirItem,
        MegalixirItem,
    ],
    discount_25=True)
shops[SH12_JUICE_BAR_SOPRANO] = Shop(
    index=12,
    items=[
        FroggieDrinkItem,
        ElixirItem,
        MegalixirItem,
        KerokeroColaItem,
    ],
    discount_50=True)
shops[SH13_SEASIDE_WEAPON] = Shop(
    index=13,
    items=[
        TroopaShellItem,
        ParasolItem,
        HurlyGlovesItem,
        DoublePunchItem,
        RibbitStickItem,
        NokNokShellItem,
        PunchGloveItem,
        FingerShotItem,
        CymbalsItem,
        ChompShellItem,
        SuperHammerItem,
        HandGunItem,
        WhompGloveItem,
        SlapGloveItem,
        LuckyHammerItem,
    ])
shops[SH14_SEASIDE_ARMOR] = Shop(
    index=14,
    items=[
        SailorShirtItem,
        SailorPantsItem,
        SailorCapeItem,
        NauticaDressItem,
        ShirtItem,
        PantsItem,
        ThickShirtItem,
        ThickPantsItem,
        MegaShirtItem,
        MegaPantsItem,
        MegaCapeItem,
        HappyShirtItem,
        HappyPantsItem,
        HappyCapeItem,
        HappyShellItem,
    ])
shops[SH15_SEASIDE_ACCESSORY] = Shop(
    index=15,
    items=[
        JumpShoesItem,
        AntidotePinItem,
        WakeUpPinItem,
        FearlessPinItem,
        TrueformPinItem,
        ZoomShoesItem,
    ])
shops[SH16_SEASIDE_HEALTH_FOOD] = Shop(
    index=16,
    items=[
        MushroomItem,
        MidMushroomItem,
        HoneySyrupItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])
shops[SH17_MONSTRO] = Shop(
    index=17,
    items=[
        SpikedLinkItem,
        CourageShellItem,
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])
shops[SH18_VOLCANO_ITEM] = Shop(
    index=18,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])
shops[SH19_VOLCANO_ARMOR] = Shop(
    index=19,
    items=[
        FireShirtItem,
        FirePantsItem,
        FireCapeItem,
        FireShellItem,
        FireDressItem,
    ])
shops[SH20_GOOMBETTE] = Shop(
    index=20,
    items=[
        MushroomItem2,
    ])
shops[SH21_NIMBUS_LAND] = Shop(
    index=21,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
        MegaGloveItem,
        WarFanItem,
        HandCannonItem,
        StickyGloveItem,
        FuzzyShirtItem,
        FuzzyPantsItem,
        FuzzyCapeItem,
        FuzzyDressItem,
    ])
shops[SH22_KEEP_1] = Shop(
    index=22,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        FreshenUpItem,
        FireShirtItem,
        FirePantsItem,
        FireCapeItem,
        FireShellItem,
        FireDressItem,
    ])
shops[SH23_KEEP_2] = Shop(
    index=23,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        FreshenUpItem,
        HeroShirtItem,
        PrincePantsItem,
        StarCapeItem,
        HealShellItem,
        RoyalDressItem,
    ])
shops[SH24_FACTORY_TOAD] = Shop(
    index=24,
    items=[
        MidMushroomItem,
        MaxMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
        FroggieDrinkItem,
    ],
    discount_50=True)
shops[SH25_DUMMY] = Shop(
    index=25,
    items=[
    ])
shops[SH26_DUMMY] = Shop(
    index=26,
    items=[
    ])
shops[SH27_DUMMY] = Shop(
    index=27,
    items=[
    ])
shops[SH28_DUMMY] = Shop(
    index=28,
    items=[
    ])
shops[SH29_DUMMY] = Shop(
    index=29,
    items=[
    ])
shops[SH30_DUMMY] = Shop(
    index=30,
    items=[
    ])
shops[SH31_DUMMY] = Shop(
    index=31,
    items=[
    ])
shops[SH32_DUMMY] = Shop(
    index=32,
    items=[
    ])

# Shop Collection
shop_collection = ShopCollection(shops)
