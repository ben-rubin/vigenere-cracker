from collections import defaultdict

# each byte in hex is represented as a 2 character string
# key is measured in multiples of chunkLen
# i.e. key length of 1 means key is 1 chunkLen or 2 characters or 1 hex byte
chunkLen = 2


def encrypt():
    key = 'mysecret'
    key_hex = [hex(ord(k)).lstrip('0x') for k in key]
    plain_text = 'rushingtostaveoffashortageofmedicalgradeprotectivegeartocombatthespreadofthecoronavirusminnesotaofficialsleanedonalocalcompanysglobalconnectionstoairliftacacheofmasksfromachinesefactorybacktothestatefordeliverythisweekwashingtonstatepurchasedcottonswabsforcoronavirusteststakingariskbecausetheproductlocatedbyofficialshasnotyetbeenapprovedbythefoodanddrugadministrationthestateisalsobettingthataseattlebasedoutdoorgearcompanyknownforitsbackpacksandparkascanreconfigureitsoperationstoproducen95respiratorsandcaliforniaactingasanationstateinthewordsofthegovernorbeganbuying200millionmaskspermonthtoshoreupsuppliesinthatstateandpotentiallyacrossthecountryadelsewheresomegovernorsandlawmakershavewatchedindisbeliefastheyhavesoughttoclosedealsonprecioussuppliesonlytohavethefederalgovernmentswoopintopreemptthearrangementsofficialsinonestatearesoworriedaboutthispossibilitythattheyareconsideringdispatchinglocalpoliceoreventhenationalguardtogreettwocharteredfedexplanesscheduledtoarriveinthenextweekwithmillionsofmasksfromchinaaccordingtopeoplefamiliarwiththeplanningthesepeoplewhospokeontheconditionofanonymityaskedthattheirstatenotbeidentifiedtoavoidflaggingfederalofficialstotheirshipmentasthetrumpadministrationassumeswhatthepresidenthascalledabackuproleindistributingsuppliestofightthepandemicstategovernmentsaretakingextraordinaryandoftenunorthodoxstepstocompeteinanincreasinglycutthroatglobalmarketplaceadsignupforourcoronavirusupdatesnewslettertotracktheoutbreakallstorieslinkedinthenewsletterarefreetoaccesstheresultisapatchworkandoftenchaoticscrambleforgoodspittingstatesagainsteachotherandoftenagainstothercountriesoreventheusgovernmentweredoingwhateveryoneelseisdoingohiogovmikedewinersaidinaninterviewyouvegot50statesandthefederalgovernmentallchasingthesamecompaniesitscrazysoaringpriceshaveleftstatesattimestopayupto10timesthenormalpricesforcertaingoodsaccordingtoofficialsfrommultiplestateseatingawayatcashreservesandlayingthefoundationforafiscalcrunchthatseveralgovernorsbelievewillrequirefederalbailoutswindfallssofargolargelytoforeigncompaniesthatmaketheequipmentalongwiththirdpartybrokersthatoftenhelpconnectstateswithmanufacturersandthengetacutaccordingtostateofficialsandbusinesspeopleadworriedaboutlosingpotentialdealsstategovernmentshavetossedasidelongstandingpurchasingrulesabouthowtospendtaxpayermoneyofferingfundsupfrontforequipmentbeforeitdisappearsgovernorsandtopaidesarespendinghoursonthephonehuntingforfriendsrelativesofaidesorotherpersonalconnectionsthatmightgivethemanedgeteamsofseniorstateaides—whoinnormaltimesoverseeissuessuchasclimatechangeandhealthpolicy—sitinconferenceroomsandbidalldaythefrenzyinvitesthepotentialforfraudaccordingtoseveralaidestogovernorswithofficialsinnewjerseyillinoismassachusettsconnecticutandwashingtonstateallsayingtheyhavebeeninundatedwithpitchesfromlikelyscamartistsohiogovmikedewineleftohiodepartmentofhealthdirectoramyactonandltgovjonhustedarriveforadailyupdateonthestatescoronavirusresponseattheohiostatehouseincolumbuslastmonthohiogovmikedewineleftohiodepartmentofhealthdirectoramyactonandltgovjonhustedarriveforadailyupdateonthestatescoronavirusresponseattheohiostatehouseincolumbuslastmonthjoshuaabickelcolumbusdispatchaphelpfromthefederalgovernmentisinconsistentwithsomegovernorshavingluckworkingwiththeirregionaldirectorsfromthefederalemergencymanagementagencyothersfindinganinwithjaredkushnerawhitehouseadviserandthepresidentssoninlawandsomeappealingdirectlytopresident'
    plain_hex = [hex(ord(pt)).lstrip('0x') for pt in plain_text]

    cypher_hex_str = ''
    for idx, ph in enumerate(plain_hex):
        cypher_hex_str += hex(int(ph, 16) ^ int(key_hex[idx % len(key_hex)], 16)).lstrip('0x')

    return cypher_hex_str


with open('cypher.txt', 'r') as f:
    cypher = f.read()
    cypherArray = [cypher[i:i + chunkLen] for i in range(0, len(cypher), chunkLen)]
    candidates = defaultdict(dict)
    totals = defaultdict(dict)

    for keyLen in range(2, 14):
        # get all streams for current key length
        candidates[keyLen] = dict(
            zip(
                [i for i in range(0, keyLen)],
                [cypherArray[i::keyLen] for i in range(0, keyLen)]
            )
        )

        for cIdx, candidate in candidates.items():
            for sIdx, stream in candidate.items():
                totals[cIdx][sIdx] = 0
                for c in (list(set(stream))):
                    totals[cIdx][sIdx] += (stream.count(c) / len(stream)) ** 2

        print('Key length: {}. Bytes: {}. IC: {}'.format(
            keyLen,
            len(stream),
            sum([val for v, val in totals[cIdx].items()]) / len(totals[cIdx]))
        )

f.close()
