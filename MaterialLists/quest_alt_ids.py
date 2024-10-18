"""
SELECT OriginalId || ': ' || NewId || ', # ' || Name
FROM 
(
SELECT q._Id as OriginalId, q2._Id as NewId, row_number() OVER(PARTITION BY q._Id order by q2._Id desc) as RowNum, t._Text as Name FROM QuestData q
JOIN QuestData q2 
	on q._QuestViewName = q2._QuestViewName 
	and q._Difficulty = q2._Difficulty
	and q._Scene01 = q2._Scene01
	and q._AreaName01 = q2._AreaName01
	and q._Id < q2._Id
join textlabel t on q._QuestViewName = t._Id
)
WHERE RowNum = 1
"""
QUEST_ALT_IDS = {
    204010101: 204580101,  # A Fervid Teacher
    204010102: 204580102,  # A Cry for Help
    204010103: 204580103,  # Magma Onslaught
    204010104: 204580104,  # The Oppressive Flame
    204010105: 204580105,  # Devotion
    204020101: 204590101,  # To the Hidden Village
    204020102: 204590102,  # Persisting on the Path
    204020103: 204590103,  # Break through the Fiends!
    204020104: 204590104,  # Melsa's Inkling
    204020105: 204590105,  # Go Forth with Courage
    204020303: 204590302,  # Hypnos Clash: Expert
    204020401: 204590401,  # Hypnos Clash EX
    204030101: 204470101,  # Watch Your Footing
    204030102: 204470102,  # Force Back the Fiends
    204030103: 204470103,  # Struggle in the Snow
    204030104: 204470104,  # Forward Without Hesitation
    204030105: 204470105,  # Banishing the Darkness Within
    204030201: 204470201,  # Manticore Assault: Beginner
    204030202: 204120202,  # Manticore Assault: Standard
    204030203: 204470202,  # Manticore Assault: Expert
    204030301: 204470301,  # Sabnock Clash: Beginner
    204030302: 204120302,  # Sabnock Clash: Standard
    204030303: 204470302,  # Sabnock Clash: Expert
    204030401: 204470401,  # Sabnock Clash EX
    204040101: 204560101,  # Fiend Clean-Up
    204040102: 204560102,  # Field Trip into Town
    204040103: 204560103,  # New Year's Eve Clash
    204040104: 204560104,  # Rescue Botan!
    204040105: 204560105,  # Moonlight March
    204040201: 204560201,  # Ieyasu's Crucible: Beginner
    204040202: 204140202,  # Ieyasu's Crucible: Standard
    204040203: 204560202,  # Ieyasu's Crucible: Expert
    204040301: 204140301,  # Shishimai Showdown: Beginner
    204040302: 204140302,  # Shishimai Showdown: Standard
    204040303: 204560302,  # Shishimai Showdown: Expert
    204040401: 204560401,  # Shishimai Showdown: EX
    204050101: 204500101,  # To the Dragon-Vein Spring
    204050102: 204500102,  # Bogged Down
    204050103: 204500103,  # Bounties for the Brave
    204050104: 204500104,  # Return to the Spring
    204050105: 204500105,  # Gaggles of Geysers
    204050201: 204500201,  # Aquatic Cyclops Assault: Beginner
    204050202: 204150202,  # Aquatic Cyclops Assault: Standard
    204050203: 204500203,  # Aquatic Cyclops Assault: Expert
    204050301: 204500301,  # Valfarre Clash: Beginner
    204050302: 204150302,  # Valfarre Clash: Standard
    204050303: 204500303,  # Valfarre Clash: Expert
    204050401: 204500401,  # Valfarre Clash EX
    204060101: 204460101,  # Save Phantom!
    204060102: 204460102,  # Twilight's Call
    204060103: 204460103,  # In the Clutches of Death
    204060104: 204460104,  # Returning Home
    204060105: 204460105,  # Fighting for Freedom
    204060201: 204460201,  # Guardian Sentinel Assault: Beginner
    204060203: 204460202,  # Guardian Sentinel Assault: Expert
    204060303: 204460302,  # Thanatos Clash: Expert
    204060401: 204460401,  # Thanatos Clash EX
    204070101: 204480101,  # The Long Journey
    204070102: 204480102,  # After the Relic
    204070201: 204480201,  # Cyclops Assault: Beginner
    204070203: 204480202,  # Cyclops Assault: Expert
    204070303: 204480302,  # Qitian Dasheng Clash: Expert
    204070401: 204480401,  # Qitian Dasheng Clash EX
    204070501: 204480501,  # Qitian Dasheng Clash: Nightmare
    204080101: 204550101,  # Pursuing the Shapeshifter
    204080102: 204550102,  # Hour of Retribution
    204080201: 204550201,  # Light Manticore Assault: Beginner
    204080202: 204550202,  # Light Manticore Assault: Expert
    204080301: 204550301,  # Aspidochelone Clash: Beginner
    204080302: 204550302,  # Aspidochelone Clash: Expert
    204080401: 204550401,  # Aspidochelone Clash EX
    204080501: 204550501,  # Aspidochelone Clash: Nightmare
    204090201: 204540201,  # Assault on Admiral Pincers: Beginner
    204090202: 204540202,  # Assault on Admiral Pincers: Expert
    204090301: 204540301,  # Scylla Clash: Beginner
    204090302: 204540302,  # Scylla Clash: Expert
    204090401: 204540401,  # Scylla Clash EX
    204090501: 204540501,  # Scylla Clash: Nightmare
    204100101: 204490101,  # Escaping the Cave
    204100102: 204490102,  # Fighting for a Chance
    204100201: 204490201,  # Defying Xuan Zang: Beginner
    204100202: 204490202,  # Defying Xuan Zang: Expert
    204100301: 204490301,  # Mei Hou Wang Clash: Beginner
    204100302: 204490302,  # Mei Hou Wang Clash: Expert
    204100401: 204490401,  # Mei Hou Wang Clash EX
    204100501: 204490501,  # Mei Hou Wang Clash: Nightmare
    204110101: 204530101,  # Tangled in Traps
    204110102: 204530102,  # The Counteroffensive
    204110201: 204530201,  # Giant Ember Toad Assault: Beginner
    204110203: 204530202,  # Giant Ember Toad Assault: Expert
    204110303: 204530302,  # Barbary Clash: Expert
    204110401: 204530401,  # Barbary Clash EX
    204110501: 204530501,  # Barbary Clash: Nightmare
    204120101: 204470101,  # Watch Your Footing
    204120102: 204470102,  # Force Back the Fiends
    204120103: 204470103,  # Struggle in the Snow
    204120104: 204470104,  # Forward Without Hesitation
    204120105: 204470105,  # Banishing the Darkness Within
    204120201: 204470201,  # Manticore Assault: Beginner
    204120203: 204470202,  # Manticore Assault: Expert
    204120301: 204470301,  # Sabnock Clash: Beginner
    204120303: 204470302,  # Sabnock Clash: Expert
    204120401: 204470401,  # Sabnock Clash EX
    204120501: 204470501,  # Sabnock Clash: Nightmare
    204130101: 204220101,  # The Unleashed Ones
    204130102: 204220102,  # A Light in the Darkness
    204130201: 204220201,  # Shining Cyclops Assault: Beginner
    204130203: 204220202,  # Shining Cyclops Assault: Expert
    204130303: 204220302,  # Chronos Clash: Expert
    204130401: 204220401,  # Chronos Nyx Clash EX
    204130501: 204220501,  # Chronos Nyx Clash: Nightmare
    204140101: 204560101,  # Fiend Clean-Up
    204140102: 204560102,  # Field Trip into Town
    204140103: 204560103,  # New Year's Eve Clash
    204140104: 204560104,  # Rescue Botan!
    204140105: 204560105,  # Moonlight March
    204140201: 204560201,  # Ieyasu's Crucible: Beginner
    204140203: 204560202,  # Ieyasu's Crucible: Expert
    204140303: 204560302,  # Shishimai Showdown: Expert
    204140401: 204560401,  # Shishimai Showdown: EX
    204140501: 204560501,  # Shishimai Showdown: Nightmare
    204150101: 204500101,  # To the Dragon-Vein Spring
    204150102: 204500102,  # Bogged Down
    204150103: 204500103,  # Bounties for the Brave
    204150104: 204500104,  # Return to the Spring
    204150105: 204500105,  # Gaggles of Geysers
    204150201: 204500201,  # Aquatic Cyclops Assault: Beginner
    204150203: 204500203,  # Aquatic Cyclops Assault: Expert
    204150301: 204500301,  # Valfarre Clash: Beginner
    204150303: 204500303,  # Valfarre Clash: Expert
    204150401: 204500401,  # Valfarre Clash EX
    204150501: 204500501,  # Valfarre Clash: Nightmare
    204160101: 204590101,  # To the Hidden Village
    204160102: 204590102,  # Persisting on the Path
    204160103: 204590103,  # Break through the Fiends!
    204160104: 204590104,  # Melsa's Inkling
    204160105: 204590105,  # Go Forth with Courage
    204160201: 204590201,  # Storm Sentinel Assault: Beginner
    204160202: 204590202,  # Storm Sentinel Assault: Expert
    204160301: 204590301,  # Hypnos Clash: Beginner
    204160302: 204590302,  # Hypnos Clash: Expert
    204160401: 204590401,  # Hypnos Clash EX
    204160501: 204590501,  # Hypnos Clash: Nightmare
    204160601: 204590601,  # Hypnos Clash: Omega (Solo)
    204160602: 204590602,  # Hypnos Clash: Omega (Raid)
    204170101: 204510101,  # Into the Woods
    204170102: 204510102,  # Wild Cat Chase
    204170201: 204510201,  # Subdue the Snapper: Beginner
    204170202: 204510202,  # Subdue the Snapper: Expert
    204170301: 204510301,  # Ebisu Showdown: Beginner
    204170302: 204510302,  # Ebisu Showdown: Expert
    204170401: 204510401,  # Ebisu Showdown EX
    204170501: 204510501,  # Ebisu Showdown: Nightmare
    204180101: 204560101,  # Fiend Clean-Up
    204180102: 204560102,  # Field Trip into Town
    204180103: 204560103,  # New Year's Eve Clash
    204180104: 204560104,  # Rescue Botan!
    204180105: 204560105,  # Moonlight March
    204180201: 204560201,  # Ieyasu's Crucible: Beginner
    204180202: 204560202,  # Ieyasu's Crucible: Expert
    204180301: 204560301,  # Shishimai Showdown: Beginner
    204180302: 204560302,  # Shishimai Showdown: Expert
    204180401: 204560401,  # Shishimai Showdown: EX
    204180501: 204560501,  # Shishimai Showdown: Nightmare
    204190101: 204500101,  # To the Dragon-Vein Spring
    204190102: 204500102,  # Bogged Down
    204190103: 204500103,  # Bounties for the Brave
    204190104: 204500104,  # Return to the Spring
    204190105: 204500105,  # Gaggles of Geysers
    204190201: 204500201,  # Aquatic Cyclops Assault: Beginner
    204190203: 204500203,  # Aquatic Cyclops Assault: Expert
    204190301: 204500301,  # Valfarre Clash: Beginner
    204190303: 204500303,  # Valfarre Clash: Expert
    204190401: 204500401,  # Valfarre Clash EX
    204190501: 204500501,  # Valfarre Clash: Nightmare
    204190601: 204500601,  # Valfarre Clash: Omega (Solo)
    204190602: 204500602,  # Valfarre Clash: Omega (Raid)
    204200101: 204580101,  # A Fervid Teacher
    204200102: 204580102,  # A Cry for Help
    204200103: 204580103,  # Magma Onslaught
    204200104: 204580104,  # The Oppressive Flame
    204200105: 204580105,  # Devotion
    204200201: 204580201,  # Assault on Archeole: Beginner
    204200203: 204580203,  # Assault on Archeole: Expert
    204200301: 204580301,  # Phraeganoth Clash: Beginner
    204200303: 204580303,  # Phraeganoth Clash: Expert
    204200401: 204580401,  # Phraeganoth Clash EX
    204200501: 204580501,  # Phraeganoth Clash: Nightmare
    204200601: 204580601,  # Phraeganoth Clash: Omega (Solo)
    204200602: 204580602,  # Phraeganoth Clash: Omega Level 1 (Raid)
    204200603: 204580603,  # Phraeganoth Clash: Omega Level 2 (Raid)
    204210101: 204530101,  # Tangled in Traps
    204210102: 204530102,  # The Counteroffensive
    204210201: 204530201,  # Giant Ember Toad Assault: Beginner
    204210202: 204530202,  # Giant Ember Toad Assault: Expert
    204210301: 204530301,  # Barbary Clash: Beginner
    204210302: 204530302,  # Barbary Clash: Expert
    204210401: 204530401,  # Barbary Clash EX
    204210501: 204530501,  # Barbary Clash: Nightmare
    204210601: 204530601,  # Barbary Clash: Omega (Solo)
    204210602: 204530602,  # Barbary Clash: Omega Level 1 (Raid)
    204210603: 204530603,  # Barbary Clash: Omega Level 2 (Raid)
    204240101: 204450101,  # A Pre-adventure Meal
    204240102: 204450102,  # Making Good Porridge
    204240201: 204450201,  # Flame Manticore Assault: Beginner
    204240202: 204450202,  # Flame Manticore Assault: Expert
    204240301: 204450301,  # Aether Clash: Beginner
    204240302: 204450302,  # Aether Clash: Expert
    204240401: 204450401,  # Aether Clash EX
    204240501: 204450501,  # Aether Clash: Nightmare
    204240601: 204450601,  # Aether Clash: Omega Level 1 (Solo)
    204240602: 204450602,  # Aether Clash: Omega Level 1 (Raid)
    204240603: 204450603,  # Aether Clash: Omega Level 2 (Solo)
    204240604: 204450604,  # Aether Clash: Omega Level 2 (Raid)
    204240605: 204450605,  # Aether Clash: Omega Level 3 (Solo)
    204240606: 204450606,  # Aether Clash: Omega Level 3 (Raid)
    204240801: 204450801,  # Pecorine's Trial
    204250101: 204420101,  # Through the Barrier
    204250102: 204420102,  # Breaking the Spell
    204250201: 204420201,  # Repelling Yoshitsune: Beginner
    204250202: 204420202,  # Repelling Yoshitsune: Expert
    204250301: 204420301,  # Shikigami Clash: Beginner
    204250302: 204420302,  # Shikigami Clash: Expert
    204250401: 204420401,  # Match with a Mischief-Maker
    204250501: 204420501,  # Shikigami Clash: Nightmare
    204250601: 204420601,  # Shikigami Clash: Omega Level 1 (Solo)
    204250602: 204420602,  # Shikigami Clash: Omega Level 1 (Raid)
    204250603: 204420603,  # Shikigami Clash: Omega Level 2 (Solo)
    204250604: 204420604,  # Shikigami Clash: Omega Level 2 (Raid)
    204250605: 204420605,  # Shikigami Clash: Omega Level 3 (Solo)
    204250606: 204420606,  # Shikigami Clash: Omega Level 3 (Raid)
    204260101: 204510101,  # Into the Woods
    204260102: 204510102,  # Wild Cat Chase
    204260201: 204510201,  # Subdue the Snapper: Beginner
    204260202: 204510202,  # Subdue the Snapper: Expert
    204260301: 204510301,  # Ebisu Showdown: Beginner
    204260302: 204510302,  # Ebisu Showdown: Expert
    204260401: 204510401,  # Ebisu Showdown EX
    204260501: 204510501,  # Ebisu Showdown: Nightmare
    204260601: 204510601,  # Ebisu Showdown: Omega Level 1 (Solo)
    204260602: 204510602,  # Ebisu Showdown: Omega Level 1 (Raid)
    204260603: 204510603,  # Ebisu Showdown: Omega Level 2 (Solo)
    204260604: 204510604,  # Ebisu Showdown: Omega Level 2 (Raid)
    204260605: 204510605,  # Ebisu Showdown: Omega Level 3 (Solo)
    204260606: 204510606,  # Ebisu Showdown: Omega Level 3 (Raid)
    204300101: 204550101,  # Pursuing the Shapeshifter
    204300102: 204550102,  # Hour of Retribution
    204300201: 204550201,  # Light Manticore Assault: Beginner
    204300202: 204550202,  # Light Manticore Assault: Expert
    204300301: 204550301,  # Aspidochelone Clash: Beginner
    204300302: 204550302,  # Aspidochelone Clash: Expert
    204300401: 204550401,  # Aspidochelone Clash EX
    204300501: 204550501,  # Aspidochelone Clash: Nightmare
    204300601: 204550601,  # Aspidochelone Clash: Omega Level 1 (Solo)
    204300602: 204550602,  # Aspidochelone Clash: Omega Level 1 (Raid)
    204300603: 204550603,  # Aspidochelone Clash: Omega Level 2 (Solo)
    204300604: 204550604,  # Aspidochelone Clash: Omega Level 2 (Raid)
    204300605: 204550605,  # Aspidochelone Clash: Omega Level 3 (Solo)
    204300606: 204550606,  # Aspidochelone Clash: Omega Level 3 (Raid)
    204310101: 204570101,  # Road to the Cathedral
    204310102: 204570102,  # Elysium Clash
    204310201: 204570201,  # Repelling Imperial Forces: Beginner
    204310202: 204570202,  # Repelling Imperial Forces: Expert
    204310301: 204570301,  # Elysium Clash: Beginner
    204310302: 204570302,  # Elysium Clash: Expert
    204310401: 204570401,  # Elysium Clash EX
    204310501: 204570501,  # Elysium Clash: Nightmare
    204310601: 204570601,  # Elysium Clash: Omega Level 1 (Solo)
    204310602: 204570602,  # Elysium Clash: Omega Level 1 (Raid)
    204310603: 204570603,  # Elysium Clash: Omega Level 2 (Solo)
    204310604: 204570604,  # Elysium Clash: Omega Level 2 (Raid)
    204310605: 204570605,  # Elysium Clash: Omega Level 3 (Solo)
    204310606: 204570606,  # Elysium Clash: Omega Level 3 (Raid)
    204320101: 204460101,  # Save Phantom!
    204320102: 204460102,  # Twilight's Call
    204320103: 204460103,  # In the Clutches of Death
    204320104: 204460104,  # Returning Home
    204320105: 204460105,  # Fighting for Freedom
    204320201: 204460201,  # Guardian Sentinel Assault: Beginner
    204320202: 204460202,  # Guardian Sentinel Assault: Expert
    204320301: 204460301,  # Thanatos Clash: Beginner
    204320302: 204460302,  # Thanatos Clash: Expert
    204320401: 204460401,  # Thanatos Clash EX
    204320501: 204460501,  # Thanatos Clash: Nightmare
    204320601: 204460601,  # Thanatos Clash: Omega Level 1 (Solo)
    204320602: 204460602,  # Thanatos Clash: Omega Level 1 (Raid)
    204320603: 204460603,  # Thanatos Clash: Omega Level 2 (Solo)
    204320604: 204460604,  # Thanatos Clash: Omega Level 2 (Raid)
    204320605: 204460605,  # Thanatos Clash: Omega Level 3 (Solo)
    204320606: 204460606,  # Thanatos Clash: Omega Level 3 (Raid)
    204330101: 204610101,  # The Forbidden Wood
    204330201: 204610201,  # Aquatic Cyclops Assault: Beginner
    204330202: 204610202,  # Aquatic Cyclops Assault: Expert
    204330301: 204610301,  # Chronos Nyx Clash: Beginner
    204330302: 204610302,  # Chronos Nyx Clash: Expert
    204330401: 204610401,  # Roar of the Mad Cyclone
    204330501: 204610501,  # Chronos Nyx Clash: Nightmare
    204330601: 204610601,  # Chronos Nyx Clash: Omega Level 1 (Solo)
    204330602: 204610602,  # Chronos Nyx Clash: Omega Level 1 (Raid)
    204330603: 204610603,  # Chronos Nyx Clash: Omega Level 2 (Solo)
    204330604: 204610604,  # Chronos Nyx Clash: Omega Level 2 (Raid)
    204330605: 204610605,  # Chronos Nyx Clash: Omega Level 3 (Solo)
    204330606: 204610606,  # Chronos Nyx Clash: Omega Level 3 (Raid)
    204340101: 204480101,  # The Long Journey
    204340102: 204480102,  # After the Relic
    204340201: 204480201,  # Cyclops Assault: Beginner
    204340202: 204480202,  # Cyclops Assault: Expert
    204340301: 204480301,  # Qitian Dasheng Clash: Beginner
    204340302: 204480302,  # Qitian Dasheng Clash: Expert
    204340401: 204480401,  # Qitian Dasheng Clash EX
    204340501: 204480501,  # Qitian Dasheng Clash: Nightmare
    204340601: 204480601,  # Qitian Dasheng Clash: Omega Level 1 (Solo)
    204340602: 204480602,  # Qitian Dasheng Clash: Omega Level 1 (Raid)
    204340603: 204480603,  # Qitian Dasheng Clash: Omega Level 2 (Solo)
    204340604: 204480604,  # Qitian Dasheng Clash: Omega Level 2 (Raid)
    204340605: 204480605,  # Qitian Dasheng Clash: Omega Level 3 (Solo)
    204340606: 204480606,  # Qitian Dasheng Clash: Omega Level 3 (Raid)
    204350101: 204520101,  # Survival Island
    204350201: 204520201,  # Assault on Commodore Pincers: Beginner
    204350202: 204520202,  # Assault on Commodore Pincers: Expert
    204350301: 204520301,  # Kanaloa Clash: Beginner
    204350302: 204520302,  # Kanaloa Clash: Expert
    204350401: 204520401,  # Kanaloa Clash EX
    204350501: 204520501,  # Kanaloa Clash: Nightmare
    204350601: 204520601,  # Kanaloa Clash: Omega Level 1 (Solo)
    204350602: 204520602,  # Kanaloa Clash: Omega Level 1 (Raid)
    204350603: 204520603,  # Kanaloa Clash: Omega Level 2 (Solo)
    204350604: 204520604,  # Kanaloa Clash: Omega Level 2 (Raid)
    204350605: 204520605,  # Kanaloa Clash: Omega Level 3 (Solo)
    204350606: 204520606,  # Kanaloa Clash: Omega Level 3 (Raid)
    204360101: 204490101,  # Escaping the Cave
    204360102: 204490102,  # Fighting for a Chance
    204360201: 204490201,  # Defying Xuan Zang: Beginner
    204360202: 204490202,  # Defying Xuan Zang: Expert
    204360301: 204490301,  # Mei Hou Wang Clash: Beginner
    204360302: 204490302,  # Mei Hou Wang Clash: Expert
    204360401: 204490401,  # Mei Hou Wang Clash EX
    204360501: 204490501,  # Mei Hou Wang Clash: Nightmare
    204360601: 204490601,  # Mei Hou Wang Clash: Omega Level 1 (Solo)
    204360602: 204490602,  # Mei Hou Wang Clash: Omega Level 1 (Raid)
    204360603: 204490603,  # Mei Hou Wang Clash: Omega Level 2 (Solo)
    204360604: 204490604,  # Mei Hou Wang Clash: Omega Level 2 (Raid)
    204360605: 204490605,  # Mei Hou Wang Clash: Omega Level 3 (Solo)
    204360606: 204490606,  # Mei Hou Wang Clash: Omega Level 3 (Raid)
    204370201: 204540201,  # Assault on Admiral Pincers: Beginner
    204370202: 204540202,  # Assault on Admiral Pincers: Expert
    204370301: 204540301,  # Scylla Clash: Beginner
    204370302: 204540302,  # Scylla Clash: Expert
    204370401: 204540401,  # Scylla Clash EX
    204370501: 204540501,  # Scylla Clash: Nightmare
    204370601: 204540601,  # Scylla Clash: Omega Level 1 (Solo)
    204370602: 204540602,  # Scylla Clash: Omega Level 1 (Raid)
    204370603: 204540603,  # Scylla Clash: Omega Level 2 (Solo)
    204370604: 204540604,  # Scylla Clash: Omega Level 2 (Raid)
    204370605: 204540605,  # Scylla Clash: Omega Level 3 (Solo)
    204370606: 204540606,  # Scylla Clash: Omega Level 3 (Raid)
    204380101: 204430101,  # Resistance of the Innocent
    204380102: 204430102,  # The Might of Heaven
    204380302: 204430302,  # Asura Clash: Expert
    204380501: 204430501,  # Asura Clash: Nightmare
    204390101: 204440101,  # Ceaseless Tragedy
    204390102: 204440102,  # A Glimmer of Hope
    204390103: 204440103,  # Satan Clash
    204390302: 204440302,  # Satan Clash: Expert
    204390501: 204440501,  # Satan Clash: Nightmare
    204400302: 204620302,  # True Bahamut Clash: Expert
    204400501: 204620501,  # True Bahamut Clash: Nightmare
    204410101: 204600101,  # The Underworld's Offensive
    204410201: 204600201,  # Water Manticore Assault: Beginner
    204410202: 204600202,  # Water Manticore Assault: Expert
    204410301: 204600301,  # Tsukuyomi Clash: Beginner
    204410302: 204600302,  # Tsukuyomi Clash: Expert
    204410401: 204600401,  # Tsukuyomi Clash EX
    204410501: 204600501,  # Tsukuyomi Clash: Nightmare
    204410601: 204600601,  # Tsukuyomi Clash: Omega Level 1 (Solo)
    204410602: 204600602,  # Tsukuyomi Clash: Omega Level 1 (Raid)
    204410603: 204600603,  # Tsukuyomi Clash: Omega Level 2 (Solo)
    204410604: 204600604,  # Tsukuyomi Clash: Omega Level 2 (Raid)
    204410605: 204600605,  # Tsukuyomi Clash: Omega Level 3 (Solo)
    204410606: 204600606,  # Tsukuyomi Clash: Omega Level 3 (Raid)
    208010101: 208210101,  # Sugar and Fiends
    208010102: 208260102,  # Trees in the Twilight
    208010103: 208210103,  # Poison Party
    208010104: 208260104,  # Lantern o' Laughs
    208010105: 208210105,  # A Fiendish Trick
    208010106: 208210106,  # A Bitter Curse
    208010107: 208210107,  # The Dead of Night
    208010301: 208260301,  # Squash the Pumpking: Beginner
    208010302: 208260302,  # Squash the Pumpking: Standard
    208010303: 208260303,  # Squash the Pumpking: Expert
    208010401: 208260401,  # Revenge of the Pumpking
    208020101: 208090101,  # Journey to the Wind Cavern
    208020102: 208180102,  # The Way Home
    208020103: 208090103,  # Perilous Puddles
    208020104: 208180104,  # Defending the Village
    208020105: 208090105,  # Danger Lurks in the Wetlands
    208020106: 208090106,  # The Great Geysers
    208020107: 208090107,  # Onward Through the Puddles
    208020301: 208180301,  # Fiend Alert: Beginner
    208020302: 208180302,  # Fiend Alert: Standard
    208020303: 208180303,  # Fiend Alert: Expert
    208020401: 208180401,  # Mega-Fiend Spotted!
    208030101: 208130101,  # Recover the Decorations!
    208030102: 208170102,  # Saintly Skirmish
    208030103: 208130103,  # Battle on the Holy Night
    208030104: 208170104,  # Trim the Treant
    208030105: 208130105,  # The Party's Centerpiece
    208030106: 208130106,  # Delivering Smiles
    208030107: 208130107,  # Don't Get Burned
    208030301: 208170301,  # Dazzling Delusions: Beginner
    208030302: 208170302,  # Dazzling Delusions: Standard
    208030303: 208170303,  # Dazzling Delusions: Expert
    208030401: 208170401,  # The Brightest Star
    208030501: 208170501,  # Season's Beatings: Expert
    208040102: 208200102,  # Practice in the Poison Swamp
    208040104: 208200104,  # A Fiendish Finale
    208040301: 208200301,  # Welcome to the Fiend Circus: Beginner
    208040302: 208200302,  # Welcome to the Fiend Circus: Standard
    208040303: 208200303,  # Welcome to the Fiend Circus: Expert
    208040401: 208200401,  # Fiend Circus Encore
    208040501: 208200501,  # Top Star Trial: Expert
    208040502: 208200502,  # Top Star Trial: Master
    208060101: 208310101,  # Seeking the Unknown
    208060102: 208310102,  # Beyond Darkness
    208060201: 208310301,  # The Crawling Nightmare: Beginner
    208060202: 208310302,  # The Crawling Nightmare: Standard
    208060203: 208310303,  # The Crawling Nightmare: Expert
    208060301: 208310401,  # It Prowls the Endless Dark...
    208060401: 208310501,  # Chaos's Calling: Expert
    208060402: 208310502,  # Chaos's Calling: Master
    208070101: 208220101,  # Fleur's Shortcut
    208070102: 208220102,  # The Search for the Egg
    208070201: 208220301,  # The Vernal Games: Beginner
    208070202: 208220302,  # The Vernal Games: Standard
    208070203: 208220303,  # The Vernal Games: Expert
    208070301: 208220401,  # The Vernal Games: Finals
    208070401: 208220501,  # Full-Bloom Festivities: Expert
    208070402: 208220502,  # Full-Bloom Festivities: Master
    208080101: 208160101,  # Finding the Master
    208080102: 208160102,  # A Deadly Drill
    208080301: 208160301,  # Arctos's Trial: Beginner
    208080302: 208160302,  # Arctos's Trial: Standard
    208080303: 208160303,  # Arctos's Trial: Expert
    208080401: 208160401,  # Arctos's Final Trial
    208080501: 208160501,  # The Path to Mastery: Expert
    208080502: 208160502,  # The Path to Mastery: Master
    208090102: 208180102,  # The Way Home
    208090104: 208180104,  # Defending the Village
    208090301: 208180301,  # Fiend Alert: Beginner
    208090302: 208180302,  # Fiend Alert: Standard
    208090303: 208180303,  # Fiend Alert: Expert
    208090401: 208180401,  # Mega-Fiend Spotted!
    208090501: 208180501,  # Ruler of the Shore: Expert
    208090502: 208180502,  # Ruler of the Shore: Master
    208100101: 208290101,  # Searching for Materials
    208100102: 208290102,  # The Opening Act
    208100301: 208290301,  # A Fiendish Performance: Beginner
    208100302: 208290302,  # A Fiendish Performance: Standard
    208100303: 208290303,  # A Fiendish Performance: Expert
    208100401: 208290401,  # A Fiendish Encore
    208100501: 208290501,  # Can't Stop the Beatdown: Expert
    208100502: 208290502,  # Can't Stop the Beatdown: Master
    208100601: 208240601,  # Can't Stop the Beatdown: Nightmare
    208110101: 208210101,  # Sugar and Fiends
    208110102: 208260102,  # Trees in the Twilight
    208110103: 208210103,  # Poison Party
    208110104: 208260104,  # Lantern o' Laughs
    208110105: 208210105,  # A Fiendish Trick
    208110106: 208210106,  # A Bitter Curse
    208110107: 208210107,  # The Dead of Night
    208110301: 208260301,  # Squash the Pumpking: Beginner
    208110302: 208260302,  # Squash the Pumpking: Standard
    208110303: 208260303,  # Squash the Pumpking: Expert
    208110401: 208260401,  # Revenge of the Pumpking
    208110501: 208260501,  # Halloween Horrors: Expert
    208110502: 208260502,  # Halloween Horrors: Master
    208110601: 208210601,  # Halloween Horrors: Nightmare
    208120101: 208310101,  # Seeking the Unknown
    208120102: 208310102,  # Beyond Darkness
    208120301: 208310301,  # The Crawling Nightmare: Beginner
    208120302: 208310302,  # The Crawling Nightmare: Standard
    208120303: 208310303,  # The Crawling Nightmare: Expert
    208120401: 208310401,  # It Prowls the Endless Dark...
    208120501: 208310501,  # Chaos's Calling: Expert
    208120502: 208310502,  # Chaos's Calling: Master
    208120601: 208270601,  # Chaos's Calling: Nightmare
    208130102: 208170102,  # Saintly Skirmish
    208130104: 208170104,  # Trim the Treant
    208130301: 208170301,  # Dazzling Delusions: Beginner
    208130302: 208170302,  # Dazzling Delusions: Standard
    208130303: 208170303,  # Dazzling Delusions: Expert
    208130401: 208170401,  # The Brightest Star
    208130501: 208170501,  # Season's Beatings: Expert
    208130502: 208170502,  # Season's Beatings: Master
    208140101: 208160101,  # Finding the Master
    208140102: 208160102,  # A Deadly Drill
    208140301: 208160301,  # Arctos's Trial: Beginner
    208140302: 208160302,  # Arctos's Trial: Standard
    208140303: 208160303,  # Arctos's Trial: Expert
    208140401: 208160401,  # Arctos's Final Trial
    208140501: 208160501,  # The Path to Mastery: Expert
    208140502: 208160502,  # The Path to Mastery: Master
    208150101: 208410101,  # Mushroom Gathering
    208150102: 208410102,  # Stocking Up for a Turnabout
    208150301: 208410301,  # Nature's Bounty - À La Carte: Beginner
    208150302: 208410302,  # Nature's Bounty - À La Carte: Standard
    208150303: 208410303,  # Nature's Bounty - À La Carte: Expert
    208150401: 208300401,  # Nature's Bounty - Full Course
    208150501: 208410501,  # Survival of the Hungriest: Expert
    208150502: 208410502,  # Survival of the Hungriest: Master
    208150601: 208300601,  # Survival of the Hungriest: Nightmare
    208190101: 208220101,  # Fleur's Shortcut
    208190102: 208220102,  # The Search for the Egg
    208190301: 208220301,  # The Vernal Games: Beginner
    208190302: 208220302,  # The Vernal Games: Standard
    208190303: 208220303,  # The Vernal Games: Expert
    208190401: 208220401,  # The Vernal Games: Finals
    208190501: 208220501,  # Full-Bloom Festivities: Expert
    208190502: 208220502,  # Full-Bloom Festivities: Master
    208210102: 208260102,  # Trees in the Twilight
    208210104: 208260104,  # Lantern o' Laughs
    208210301: 208260301,  # Squash the Pumpking: Beginner
    208210302: 208260302,  # Squash the Pumpking: Standard
    208210303: 208260303,  # Squash the Pumpking: Expert
    208210401: 208260401,  # Revenge of the Pumpking
    208210501: 208260501,  # Halloween Horrors: Expert
    208210502: 208260502,  # Halloween Horrors: Master
    208230101: 208420101,  # A Sudden Attack
    208230102: 208420102,  # Protect the Stage!
    208230301: 208420301,  # Frenetic Fiend Festival: Beginner
    208230302: 208420302,  # Frenetic Fiend Festival: Standard
    208230303: 208420303,  # Frenetic Fiend Festival: Expert
    208230401: 208360401,  # Fiend Festival Finale
    208230501: 208420501,  # Raging Festivities: Expert
    208230502: 208420502,  # Raging Festivities: Master
    208230601: 208360601,  # Raging Festivities: Nightmare
    208240101: 208290101,  # Searching for Materials
    208240102: 208290102,  # The Opening Act
    208240301: 208290301,  # A Fiendish Performance: Beginner
    208240302: 208290302,  # A Fiendish Performance: Standard
    208240303: 208290303,  # A Fiendish Performance: Expert
    208240401: 208290401,  # A Fiendish Encore
    208240501: 208290501,  # Can't Stop the Beatdown: Expert
    208240502: 208290502,  # Can't Stop the Beatdown: Master
    208250101: 208390101,  # Subduing the Beasts
    208250301: 208390301,  # The Goddess's Will: Beginner
    208250302: 208390302,  # The Goddess's Will: Standard
    208250303: 208390303,  # The Goddess's Will: Expert
    208250304: 208390304,  # Smiting the Haughty Demon: Standard
    208250305: 208390305,  # Smiting the Haughty Demon: Expert
    208250401: 208350401,  # The Goddess's Will: Reckoning
    208250501: 208390501,  # Divine Deliverance: Expert
    208250502: 208390502,  # Divine Deliverance: Master
    208250601: 208350601,  # Divine Deliverance: Nightmare
    208270101: 208310101,  # Seeking the Unknown
    208270102: 208310102,  # Beyond Darkness
    208270301: 208310301,  # The Crawling Nightmare: Beginner
    208270302: 208310302,  # The Crawling Nightmare: Standard
    208270303: 208310303,  # The Crawling Nightmare: Expert
    208270401: 208310401,  # It Prowls the Endless Dark...
    208270501: 208310501,  # Chaos's Calling: Expert
    208270502: 208310502,  # Chaos's Calling: Master
    208280101: 208430101,  # Welcome to the Blue Rose's Show
    208280301: 208430301,  # Fiend Opera Overture: Beginner
    208280302: 208430302,  # Fiend Opera Overture: Standard
    208280303: 208430303,  # Fiend Opera Overture: Expert
    208280401: 208400401,  # Fiend Opera Finale
    208280501: 208430501,  # Fiend Opera Gala: Expert
    208280502: 208430502,  # Fiend Opera Gala: Master
    208280601: 208400601,  # Fiend Opera Gala: Nightmare
    208280701: 208430701,  # A Duel with the Phantom Thief: Standard
    208280702: 208430702,  # A Duel with the Phantom Thief: Expert
    208300101: 208410101,  # Mushroom Gathering
    208300102: 208410102,  # Stocking Up for a Turnabout
    208300301: 208410301,  # Nature's Bounty - À La Carte: Beginner
    208300302: 208410302,  # Nature's Bounty - À La Carte: Standard
    208300303: 208410303,  # Nature's Bounty - À La Carte: Expert
    208300501: 208410501,  # Survival of the Hungriest: Expert
    208300502: 208410502,  # Survival of the Hungriest: Master
    208330101: 208440101,  # The False Demon's Revenge
    208330301: 208440301,  # Active Investigation: Beginner
    208330302: 208440302,  # Active Investigation: Standard
    208330303: 208440303,  # Active Investigation: Expert
    208330401: 208380401,  # Aggressive Investigation
    208330501: 208440501,  # In Pursuit of Truth: Expert
    208330502: 208440502,  # In Pursuit of Truth: Master
    208330601: 208380601,  # In Pursuit of Truth: Nightmare
    208330701: 208440701,  # Judgment for the Wicked: Standard
    208330702: 208440702,  # Judgment for the Wicked: Expert
    208340101: 208450101,  # Wrath of Leviathan
    208340301: 208450301,  # The Stirring Abyss: Beginner
    208340302: 208450302,  # The Stirring Abyss: Standard
    208340303: 208450303,  # The Stirring Abyss: Expert
    208340501: 208450501,  # Tempestuous Assault: Expert
    208340502: 208450502,  # Tempestuous Assault: Master
    208340701: 208450701,  # Wrath of Leviathan: Standard
    208340702: 208450702,  # Wrath of Leviathan: Expert
    208350101: 208390101,  # Subduing the Beasts
    208350301: 208390301,  # The Goddess's Will: Beginner
    208350302: 208390302,  # The Goddess's Will: Standard
    208350303: 208390303,  # The Goddess's Will: Expert
    208350304: 208390304,  # Smiting the Haughty Demon: Standard
    208350305: 208390305,  # Smiting the Haughty Demon: Expert
    208350501: 208390501,  # Divine Deliverance: Expert
    208350502: 208390502,  # Divine Deliverance: Master
    208360101: 208420101,  # A Sudden Attack
    208360102: 208420102,  # Protect the Stage!
    208360301: 208420301,  # Frenetic Fiend Festival: Beginner
    208360302: 208420302,  # Frenetic Fiend Festival: Standard
    208360303: 208420303,  # Frenetic Fiend Festival: Expert
    208360501: 208420501,  # Raging Festivities: Expert
    208360502: 208420502,  # Raging Festivities: Master
    208370101: 208460101,  # The Hunt for Medicinal Herbs
    208370301: 208460301,  # Choreography Class: Beginner
    208370302: 208460302,  # Choreography Class: Standard
    208370303: 208460303,  # Choreography Class: Expert
    208370501: 208460501,  # Theatrical Throwdown: Expert
    208370502: 208460502,  # Theatrical Throwdown: Master
    208370701: 208460701,  # The Creature's Curtain Call: Standard
    208370702: 208460702,  # The Creature's Curtain Call: Expert
    208380101: 208440101,  # The False Demon's Revenge
    208380301: 208440301,  # Active Investigation: Beginner
    208380302: 208440302,  # Active Investigation: Standard
    208380303: 208440303,  # Active Investigation: Expert
    208380501: 208440501,  # In Pursuit of Truth: Expert
    208380502: 208440502,  # In Pursuit of Truth: Master
    208380701: 208440701,  # Judgment for the Wicked: Standard
    208380702: 208440702,  # Judgment for the Wicked: Expert
    208400101: 208430101,  # Welcome to the Blue Rose's Show
    208400301: 208430301,  # Fiend Opera Overture: Beginner
    208400302: 208430302,  # Fiend Opera Overture: Standard
    208400303: 208430303,  # Fiend Opera Overture: Expert
    208400501: 208430501,  # Fiend Opera Gala: Expert
    208400502: 208430502,  # Fiend Opera Gala: Master
    208400701: 208430701,  # A Duel with the Phantom Thief: Standard
    208400702: 208430702,  # A Duel with the Phantom Thief: Expert
    214010101: 214040101,  # Repel the Empire! (Normal)
    214010102: 214040102,  # Repel the Empire! (Hard)
    214010103: 214040103,  # Repel the Empire! (Lunatic)
    214010104: 214040104,  # Repel the Empire! (Infernal)
    214010105: 214040105,  # Repel the Empire!
    214010201: 214040201,  # The Prince from Another World
    214010202: 214040202,  # The Reticent Princess
    214010203: 214040203,  # Alfonse's Trial
    214010204: 214040204,  # Veronica's Trial
    214010301: 214040301,  # The Alberian Front (Normal)
    214010302: 214040302,  # The Alberian Front (Hard)
    214010303: 214040303,  # The Alberian Front (Lunatic)
    214020101: 214040101,  # Repel the Empire! (Normal)
    214020102: 214040102,  # Repel the Empire! (Hard)
    214020103: 214040103,  # Repel the Empire! (Lunatic)
    214020104: 214040104,  # Repel the Empire! (Infernal)
    214020105: 214040105,  # Repel the Empire!
    214020201: 214040201,  # The Prince from Another World
    214020202: 214040202,  # The Reticent Princess
    214020203: 214040203,  # Alfonse's Trial
    214020204: 214040204,  # Veronica's Trial
    214020301: 214040301,  # The Alberian Front (Normal)
    214020302: 214040302,  # The Alberian Front (Hard)
    214020303: 214040303,  # The Alberian Front (Lunatic)
    214030101: 214050101,  # Sweet Dream
    214030102: 214050102,  # Dragon Scion
    214030103: 214050103,  # Prince of Ylisse
    214030201: 214050201,  # Battle with Peony (Normal)
    214030202: 214050202,  # Battle with Peony (Hard)
    214030301: 214050301,  # Battle with Tiki (Normal)
    214030302: 214050302,  # Battle with Tiki (Hard)
    214030401: 214050401,  # Battle with Chrom (Normal)
    214030402: 214050402,  # Battle with Chrom (Hard)
    214030501: 214050501,  # Peony's Trial
    214030502: 214050502,  # Tiki's Trial
    214030503: 214050503,  # Chrom's Trial
    214030601: 214050601,  # Thórr's Descent (Normal)
    214030602: 214050602,  # Thórr's Descent (Hard)
    214030603: 214050603,  # Thórr's Descent (Lunatic)
    214030604: 214050604,  # Thórr's Hammer
    214031101: 214051101,  # Arena of Flame (Normal)
    214031102: 214051102,  # Arena of Flame (Hard)
    214031103: 214051103,  # Arena of Flame (Lunatic)
    214031104: 214051104,  # Arena of Flame (Infernal)
    214031201: 214051201,  # Arena of Water (Normal)
    214031202: 214051202,  # Arena of Water (Hard)
    214031203: 214051203,  # Arena of Water (Lunatic)
    214031204: 214051204,  # Arena of Water (Infernal)
    214031301: 214051301,  # Arena of Wind (Normal)
    214031302: 214051302,  # Arena of Wind (Hard)
    214031303: 214051303,  # Arena of Wind (Lunatic)
    214031304: 214051304,  # Arena of Wind (Infernal)
    214031401: 214051401,  # Arena of Light (Normal)
    214031402: 214051402,  # Arena of Light (Hard)
    214031403: 214051403,  # Arena of Light (Lunatic)
    214031404: 214051404,  # Arena of Light (Infernal)
    214031501: 214051501,  # Arena of Shadow (Normal)
    214031502: 214051502,  # Arena of Shadow (Hard)
    214031503: 214051503,  # Arena of Shadow (Lunatic)
    214031504: 214051504,  # Arena of Shadow (Infernal)
    222010101: 222250101,  # Skirmish: Beginner
    222010102: 222250102,  # Local Conflict: Beginner
    222010103: 222250103,  # All-Out Assault: Beginner
    222010201: 222250201,  # Skirmish: Standard
    222010202: 222250202,  # Local Conflict: Standard
    222010203: 222250203,  # All-Out Assault: Standard
    222010301: 222250301,  # Skirmish: Expert
    222010302: 222250302,  # Local Conflict: Expert
    222010303: 222250303,  # All-Out Assault: Expert
    222010401: 222250401,  # Skirmish: Master
    222010402: 222250402,  # Local Conflict: Master
    222010403: 222250403,  # All-Out Assault: Master
    222010404: 222250404,  # All-Out Assault EX
    222020101: 222190101,  # Skirmish: Beginner
    222020102: 222190102,  # Local Conflict: Beginner
    222020103: 222190103,  # Defensive Battle: Beginner
    222020201: 222190201,  # Skirmish: Standard
    222020202: 222190202,  # Local Conflict: Standard
    222020203: 222190203,  # Defensive Battle: Standard
    222020301: 222190301,  # Skirmish: Expert
    222020302: 222190302,  # Local Conflict: Expert
    222020303: 222190303,  # Defensive Battle: Expert
    222020401: 222190401,  # Skirmish: Master
    222020402: 222190402,  # Local Conflict: Master
    222020403: 222190403,  # Defensive Battle: Master
    222020404: 222190404,  # Defensive Battle EX
    222030101: 222200101,  # Skirmish: Beginner
    222030102: 222200102,  # Local Conflict: Beginner
    222030103: 222200103,  # All-Out Assault: Beginner
    222030201: 222200201,  # Skirmish: Standard
    222030202: 222200202,  # Local Conflict: Standard
    222030203: 222200203,  # All-Out Assault: Standard
    222030301: 222200301,  # Skirmish: Expert
    222030302: 222200302,  # Local Conflict: Expert
    222030303: 222200303,  # All-Out Assault: Expert
    222030401: 222200401,  # Skirmish: Master
    222030402: 222200402,  # Local Conflict: Master
    222030403: 222200403,  # All-Out Assault: Master
    222030404: 222200404,  # All-Out Assault EX
    222030405: 222200405,  # Astral High Midgardsormr Assault
    222040101: 222280101,  # Skirmish: Beginner
    222040102: 222280102,  # Local Conflict: Beginner
    222040103: 222280103,  # Defensive Battle: Beginner
    222040201: 222280201,  # Skirmish: Standard
    222040202: 222280202,  # Local Conflict: Standard
    222040203: 222280203,  # Defensive Battle: Standard
    222040301: 222280301,  # Skirmish: Expert
    222040302: 222280302,  # Local Conflict: Expert
    222040303: 222280303,  # Defensive Battle: Expert
    222040401: 222280401,  # Skirmish: Master
    222040402: 222280402,  # Local Conflict: Master
    222040403: 222280403,  # Defensive Battle: Master
    222040404: 222280404,  # Defensive Battle EX
    222060101: 222290101,  # Skirmish: Beginner
    222060102: 222290102,  # Local Conflict: Beginner
    222060103: 222290103,  # Defensive Battle: Beginner
    222060201: 222290201,  # Skirmish: Standard
    222060202: 222290202,  # Local Conflict: Standard
    222060203: 222290203,  # Defensive Battle: Standard
    222060301: 222290301,  # Skirmish: Expert
    222060302: 222290302,  # Local Conflict: Expert
    222060303: 222290303,  # Defensive Battle: Expert
    222060401: 222290401,  # Skirmish: Master
    222060402: 222290402,  # Local Conflict: Master
    222060403: 222290403,  # Defensive Battle: Master
    222060404: 222290404,  # Defensive Battle EX
    222060405: 222290405,  # Defensive Battle: Field Training
    222070101: 222180101,  # Skirmish: Beginner
    222070102: 222180102,  # Local Conflict: Beginner
    222070103: 222180103,  # All-Out Assault: Beginner
    222070201: 222180201,  # Skirmish: Standard
    222070202: 222180202,  # Local Conflict: Standard
    222070203: 222180203,  # All-Out Assault: Standard
    222070301: 222180301,  # Skirmish: Expert
    222070302: 222180302,  # Local Conflict: Expert
    222070303: 222180303,  # All-Out Assault: Expert
    222070401: 222180401,  # Skirmish: Master
    222070402: 222180402,  # Local Conflict: Master
    222070403: 222180403,  # All-Out Assault: Master
    222070404: 222180404,  # All-Out Assault EX
    222070405: 222180405,  # Astral High Jupiter Assault
    222080101: 222210101,  # First Preliminary Round: Beginner
    222080102: 222210102,  # Second Preliminary Round: Beginner
    222080103: 222210103,  # First Round of the Tournament
    222080201: 222210201,  # First Preliminary Round: Standard
    222080202: 222210202,  # Second Preliminary Round: Standard
    222080203: 222210203,  # Second Round of the Tournament
    222080301: 222210301,  # First Preliminary Round: Expert
    222080302: 222210302,  # Second Preliminary Round: Expert
    222080303: 222210303,  # Third Round of the Tournament
    222080401: 222210401,  # First Preliminary Round: Master
    222080402: 222210402,  # Second Preliminary Round: Master
    222080403: 222210403,  # Tournament Finals
    222080404: 222210404,  # Exhibition Match EX
    222080405: 222210405,  # Exhibition Match: Encore EX
    222090101: 222220101,  # Skirmish: Beginner
    222090102: 222220102,  # Local Conflict: Beginner
    222090103: 222220103,  # All-Out Assault: Beginner
    222090201: 222220201,  # Skirmish: Standard
    222090202: 222220202,  # Local Conflict: Standard
    222090203: 222220203,  # All-Out Assault: Standard
    222090301: 222220301,  # Skirmish: Expert
    222090302: 222220302,  # Local Conflict: Expert
    222090303: 222220303,  # All-Out Assault: Expert
    222090401: 222220401,  # Skirmish: Master
    222090402: 222220402,  # Local Conflict: Master
    222090403: 222220403,  # All-Out Assault: Master
    222090404: 222220404,  # All-Out Assault EX
    222090405: 222220405,  # Astral High Brunhilda Assault
    222100101: 222300101,  # Skirmish: Beginner
    222100102: 222300102,  # Local Conflict: Beginner
    222100103: 222300103,  # Defensive Battle: Beginner
    222100201: 222300201,  # Skirmish: Standard
    222100202: 222300202,  # Local Conflict: Standard
    222100203: 222300203,  # Defensive Battle: Standard
    222100301: 222300301,  # Skirmish: Expert
    222100302: 222300302,  # Local Conflict: Expert
    222100303: 222300303,  # Defensive Battle: Expert
    222100401: 222300401,  # Skirmish: Master
    222100402: 222300402,  # Local Conflict: Master
    222100403: 222300403,  # Defensive Battle: Master
    222100404: 222300404,  # Defensive Battle EX
    222100405: 222300405,  # Defensive Battle: Field Training
    222110101: 222240101,  # Skirmish: Beginner
    222110102: 222240102,  # Local Conflict: Beginner
    222110103: 222240103,  # All-Out Assault: Beginner
    222110201: 222240201,  # Skirmish: Standard
    222110202: 222240202,  # Local Conflict: Standard
    222110203: 222240203,  # All-Out Assault: Standard
    222110301: 222240301,  # Skirmish: Expert
    222110302: 222240302,  # Local Conflict: Expert
    222110303: 222240303,  # All-Out Assault: Expert
    222110401: 222240401,  # Skirmish: Master
    222110402: 222240402,  # Local Conflict: Master
    222110403: 222240403,  # All-Out Assault: Master
    222110404: 222240404,  # All-Out Assault EX
    222110405: 222240405,  # Astral High Zodiark Assault
    222120101: 222230101,  # Skirmish: Beginner
    222120102: 222230102,  # Local Conflict: Beginner
    222120103: 222230103,  # Defensive Battle: Beginner
    222120201: 222230201,  # Skirmish: Standard
    222120202: 222230202,  # Local Conflict: Standard
    222120203: 222230203,  # Defensive Battle: Standard
    222120301: 222230301,  # Skirmish: Expert
    222120302: 222230302,  # Local Conflict: Expert
    222120303: 222230303,  # Defensive Battle: Expert
    222120401: 222230401,  # Skirmish: Master
    222120402: 222230402,  # Local Conflict: Master
    222120403: 222230403,  # Defensive Battle: Master
    222120404: 222230404,  # Defensive Battle EX
    222120405: 222230405,  # Defensive Battle: Field Training
    222130101: 222260101,  # Skirmish: Beginner
    222130102: 222260102,  # Local Conflict: Beginner
    222130103: 222260103,  # All-Out Assault: Beginner
    222130201: 222260201,  # Skirmish: Standard
    222130202: 222260202,  # Local Conflict: Standard
    222130203: 222260203,  # All-Out Assault: Standard
    222130301: 222260301,  # Skirmish: Expert
    222130302: 222260302,  # Local Conflict: Expert
    222130303: 222260303,  # All-Out Assault: Expert
    222130401: 222260401,  # Skirmish: Master
    222130402: 222260402,  # Local Conflict: Master
    222130403: 222260403,  # All-Out Assault: Master
    222130404: 222260404,  # All-Out Assault EX
    222130405: 222260405,  # Astral Ciella Assault
    222140101: 222310101,  # Skirmish: Beginner
    222140102: 222310102,  # Local Conflict: Beginner
    222140103: 222310103,  # Defensive Battle: Beginner
    222140201: 222310201,  # Skirmish: Standard
    222140202: 222310202,  # Local Conflict: Standard
    222140203: 222310203,  # Defensive Battle: Standard
    222140301: 222310301,  # Skirmish: Expert
    222140302: 222310302,  # Local Conflict: Expert
    222140303: 222310303,  # Defensive Battle: Expert
    222140401: 222310401,  # Skirmish: Master
    222140402: 222310402,  # Local Conflict: Master
    222140403: 222310403,  # Defensive Battle: Master
    222140404: 222310404,  # Defensive Battle EX
    222140405: 222310405,  # Defensive Battle: Field Training
    222150101: 222320101,  # Skirmish: Beginner
    222150102: 222320102,  # Local Conflict: Beginner
    222150103: 222320103,  # All-Out Assault: Beginner
    222150201: 222320201,  # Skirmish: Standard
    222150202: 222320202,  # Local Conflict: Standard
    222150203: 222320203,  # All-Out Assault: Standard
    222150301: 222320301,  # Skirmish: Expert
    222150302: 222320302,  # Local Conflict: Expert
    222150303: 222320303,  # All-Out Assault: Expert
    222150401: 222320401,  # Skirmish: Master
    222150402: 222320402,  # Local Conflict: Master
    222150403: 222320403,  # All-Out Assault: Master
    222150404: 222320404,  # All-Out Assault EX
    222150405: 222320405,  # Astral Volk Assault
    222160101: 222330101,  # Skirmish: Beginner
    222160102: 222330102,  # Local Conflict: Beginner
    222160103: 222330103,  # Defensive Battle: Beginner
    222160201: 222330201,  # Skirmish: Standard
    222160202: 222330202,  # Local Conflict: Standard
    222160203: 222330203,  # Defensive Battle: Standard
    222160301: 222330301,  # Skirmish: Expert
    222160302: 222330302,  # Local Conflict: Expert
    222160303: 222330303,  # Defensive Battle: Expert
    222160401: 222330401,  # Skirmish: Master
    222160402: 222330402,  # Local Conflict: Master
    222160403: 222330403,  # Defensive Battle: Master
    222160404: 222330404,  # Defensive Battle EX
    222160405: 222330405,  # Defensive Battle: Field Training
    222170101: 222270101,  # Skirmish: Beginner
    222170102: 222270102,  # Local Conflict: Beginner
    222170103: 222270103,  # All-Out Assault: Beginner
    222170201: 222270201,  # Skirmish: Standard
    222170202: 222270202,  # Local Conflict: Standard
    222170203: 222270203,  # All-Out Assault: Standard
    222170301: 222270301,  # Skirmish: Expert
    222170302: 222270302,  # Local Conflict: Expert
    222170303: 222270303,  # All-Out Assault: Expert
    222170401: 222270401,  # Skirmish: Master
    222170402: 222270402,  # Local Conflict: Master
    222170403: 222270403,  # All-Out Assault: Master
    222170404: 222270404,  # All-Out Assault EX
    222170405: 222270405,  # Astral Tartarus Assault
    227090101: 227110101,  # Battle at Myriage Lake: Beginner
    227090102: 227110102,  # Void Poseidon Strike: Standard
    227090103: 227110103,  # High Mercury's Trial: Expert
    227090104: 227110104,  # High Mercury's Trial: Master
    227090105: 227110105,  # Iblis's Surging Cascade (Ranked)
    229010101: 229060101,  # Battle for Yggdrasil
    229010201: 229060201,  # Repelling the Forest's Aggressors: Standard
    229010202: 229060202,  # Repelling the Forest's Aggressors: Expert
    229010203: 229060203,  # Repelling the Forest's Aggressors: Master
    229010301: 229060301,  # Guardians of the Wood: Standard
    229010302: 229060302,  # Guardians of the Wood: Expert
    229010303: 229060303,  # Guardians of the Wood: Master
    229010401: 229060401,  # The Blessings of Yggdrasil
    229011201: 229061201,  # Repelling the Forest's Aggressors: Standard
    229011202: 229061202,  # Repelling the Forest's Aggressors: Expert
    229011203: 229061203,  # Repelling the Forest's Aggressors: Master
    229011301: 229061301,  # Guardians of the Wood: Standard
    229011302: 229061302,  # Guardians of the Wood: Expert
    229011303: 229061303,  # Guardians of the Wood: Master
    229020101: 229070101,  # White Sparrow VS Black Raven
    229020201: 229070201,  # Repelling the Forces of Grams: Standard
    229020202: 229070202,  # Repelling the Forces of Grams: Expert
    229020203: 229070203,  # Repelling the Forces of Grams: Master
    229020301: 229070301,  # A Duel with the Black Raven: Standard
    229020302: 229070302,  # A Duel with the Black Raven: Expert
    229020303: 229070303,  # A Duel with the Black Raven: Master
    229020401: 229070401,  # The Great Grams Escape
    229021201: 229071201,  # Repelling the Forces of Grams: Standard
    229021202: 229071202,  # Repelling the Forces of Grams: Expert
    229021203: 229071203,  # Repelling the Forces of Grams: Master
    229021301: 229071301,  # A Duel with the Black Raven: Standard
    229021302: 229071302,  # A Duel with the Black Raven: Expert
    229021303: 229071303,  # A Duel with the Black Raven: Master
    230010101: 310020101,  # Walkies
    300010101: 301010101,  # Wandering Shroom Strike
    300020101: 301030101,  # Frost Hermit Strike
    300030101: 301040101,  # Steel Golem Strike
    300050101: 301070101,  # Raging Manticore Strike
    300060101: 301020101,  # Blazing Ghost Strike
    300070101: 301040102,  # Obsidian Golem Strike
    300090101: 301010102,  # Gust Shroom Strike
    300100101: 301020102,  # Violet Ghost Strike
    300110101: 301040103,  # Amber Golem Strike
    300140101: 301070102,  # Greedy Manticore Strike
    300150101: 301010103,  # Scalding Shroom Strike
    300160101: 301030102,  # Twilight Hermit Strike
    300170101: 301050101,  # Catoblepas Anemos Strike
    300190101: 301020103,  # Lambent Ghost Strike
    300200101: 301060101,  # Eolian Phantom Strike
    300210101: 301070103,  # Smoldering Manticore Strike
    300230101: 301070104,  # Proud Manticore Strike
    300250101: 301020104,  # Cerulean Ghost Strike
    300260101: 301050102,  # Catoblepas Fotia Strike
    300270101: 301060102,  # Infernal Phantom Strike
    310010101: 310070101,  # Treasure Slime Clean-Up
    310010201: 310070201,  # Fafnir Clean-Up
    310010301: 310070301,  # Gold Slime Clean-Up
    310030101: 310060101,  # Ascent to Power
    310030201: 310060201,  # Ascent to Fortune
    310040101: 310070101,  # Treasure Slime Clean-Up
    310040201: 310070201,  # Fafnir Clean-Up
    310040301: 310070301,  # Gold Slime Clean-Up
    310050101: 310060101,  # Ascent to Power
    310050201: 310060201,  # Ascent to Fortune
}
