from math import inf
from dataclasses import dataclass


@dataclass
class Limit:
    lower: int
    upper: int | float = inf

    def is_valid_length(self, value):
        return self.lower <= value <= self.upper


@dataclass
class Category:
    name: str
    limit: Limit
    words: tuple[str]
    not_words: tuple[str] = tuple()
    other_words: tuple[str] = tuple()


title_words = (
    "in short", "result",
    "summary", "objective",  "keyword",
    "key points", "category",
    "motivation", "rationale", "background",
    "tl;dr", "tldr", "tl,dr", "tl;dr:"
    "benefit", "recommendation", "purpose",
    "the proposal",
    "goal", " aim ", "conclusion",
    "synopsis", "abstract",
    # "therefore" <-> here
    # "solution",
    # aim <-> claim
)


other_title_words = (
    "problem", "disclaimer", "introduction", "method", "methodology",
    "result", "discussion", "acknowledgement", "reference",
    "appendi", "author",
    "detail", "specification", "requirement", "implementation",
    "contribution", "analysis", "evaluation",
    "content", "overview", "review", "means", "mechanism",
    "drawback", "limitation", "challenge", "issue", "concern",
    "vote", "overall cost", "risk", "candidate",
    "responssibilit",  "description", "why", "when",
    "parameter", "solution"
)

not_title_words = (
    "other", "detail"
)

sentence_words = (
    "i propose", "we propose", "i suggest", "we suggest",
    "i recommend", "we recommend",
    "proposes to", "suggests to", "recommends to",
    "to propose", "to suggest", "to recommend",
    # "we should", "we must",
    "therefore",
)

not_sentence = (
    "Link to proposed Governance Update",
    "[Read the original proposal on Discourse](",
    "Read the formatted version of this proposal at",
    "[This proposal is also on Balancer's forum](",
    "[Link to proposal discussion](",
)

categories = dict(
    title=Category(
        name="title",
        words=title_words,
        not_words=not_title_words,
        other_words=other_title_words,
        limit=Limit(lower=2, upper=30)
    ),
    sentence=Category(
        name="sentence",
        words=sentence_words,
        limit=Limit(lower=30)
    ),
)


body_for_sim = {
    "replace": {
        "common": {
            "tl;dr": "tldr",
            "author:": "author",
            "summary:": "summary",
            "disclaimer:": "disclaimer",
            "specfication:": "specification",
            # "specifications": "specification",
            # "authors": "author",
        }
    },
    "deleted": {
        "common": [
            "Copyright",
            "and related rights waived via",
            "and related rights waived under",
            "[CC0](", "CC0.", "CC0,",
            "[Creative Commons Zero (CC0)](",
            "Creative Commons Zero (CC0)",
            "PUBLIC AIRDROP INFOMATION:",
            "Good luck",
            "Read more:",
            "[](", "[ ](",
            "[Link](",
            "[Image source](",
            "[Link to proposal discussion](",
            "Link to Discussions:",
            "*[This proposal is summarized due to technical limitations. To view it complete and vote on it, visit the DCL DAO Governance dApp](",
        ],
        "specific": {
            "mocana.eth": [
                "-------------- ApeCoin DAO Snapshot Contents --------------",
                "------------ ApeCoin DAO Snapshot Contents --------------",
                "The below contents are duplicated from the ApeCoin DAO Snapshot:",
                "The below contents are duplicated from ApeCoin DAO's Snapshot Space, which you can view on this original link:",
                "Moca DAO members will vote with their Mocaverse NFTs here on our Moca DAO Snapshot Space. Based on those results, delegated voting will then be carried out on the ApeCoin DAO Snapshot Space with the Mocaverseape.eth multi-signature wallet.",
                "Moca DAO members will vote with Mocaverse NFTs on our Moca DAO Snapshot Space. Delegated voting will then be done on the ApeCoin DAO Snapshot Space with the Mocaverseape.eth wallet.",
                "Members will vote with Moca NFTs on our Moca Snapshot. Delegated voting will then be done on the ApeCoin DAO Snapshot with the Mocaverseape.eth wallet.",
                "Read, research, discuss - See what you think, fellow Mocas! Make your voices heard.",
                "Link to the full proposal:",
                "The AIP implementation is administered by the Ape Foundation. Implementation may be immaterially or materially altered to optimise for security, usability, to protect APE holders, and otherwise to effect the intent of the AIP. Any material deviations from an AIP, as initially approved, will be disclosed to the APE holder community."
            ],
            "balancer.eth": [
                "[This proposal is also on Balancer's forum.](",
                "PR with Payload", "Payload with PR",
                "This proposal appears on [Balancer's forum](",
                "This proposal also appears on [Balancer's forum](",
                "Protocol Description:",
                "References/Useful links:", "References/Useful links",
                "References\n[Balancer Deployments](\n[BAL Addresses](",
                ">", "[](", "> >",
                "* [Documentation of E-CLPs](",
                "* [Website](",
                "* [Github](",
                "* [Discord](",
                "* [X](",
            ],
            "sushigov.eth": [
                "Full details and discussions thus far can be found at:",
            ],
            "aave.eth": [
                "TokenLogic and karpatkey receive no payment for this proposal. TokenLogic and karpatkey are both delegates within the Aave community.",
                "Disclaimer Gauntlet reserves the right to not move forward with any parameter changes recommended in Snapshot polls, if market conditions change meaningfully.",
                "By approving this proposal, you agree that any services provided by Gauntlet shall be governed by the terms of service available at gauntlet.network/tos",
                "The ACI is not presenting this ARFC on behalf of any third party and is not compensated for creating this ARFC.",
                "[Forum Discussion](",
                "For more details, please see [Gauntlet's Parameter Recommendation Methodology]( and [Gauntlet's Model Methodology](",
                ":", "**", "*:*"
            ],
            "aavegotchi.eth": [
                "Author:", "Gotchi ID:", "Authors:",
                "Jesse | gldnXross", "Dr Wagmi", "Maxicrouton",
                "**",
            ],
            "diadao.eth": [
                "[See source](",
                "Learn more at",
            ],
            "index-coop.eth": [
                "using DPI.", "using Index Products.",
                "Quorum for this vote is ",
                "This proposal is for voting on Uniswap's proposal",
                "This MetaGovernance vote is for voting on Compound's latest proposal using Index Products.",
                "This MetaGovernance vote is for voting on Uniswap's latest proposal using Index Products.",
                "This MetaGovernance vote is for voting on Uniswap's latest proposal using UNI locked in Index Products.",
                "Index holder'as voting power is ~5% of the Uniswap proposal quorum",
                "This MetaGovernance vote is for voting on Uniswap's latest proposal using Index Products.",
                "This proposal is for voting on Aave's proposal",
                "This proposal is for voting on Compound's proposal",
                "The quorum for this vote is ", "INDEX.", "INDEX - *[5% Circulating Supply](",
                "Please review the proposal here:",
                "Please review the proposal in the link bellow",
                "Please review the governance discussion of the proposal in the link below:",
                "Please review the on-chain vote of the proposal in the link below:",
                "*(", "Source [",
            ],
            # "gnosis.eth": [
            # ],
            "idlefinance.eth": [
                "Other References:",
                "- [A Step Towards Idle Leagues  Dev & Treasury](\n- [About Idle Leagues](",
                "* [Set up an initial Treasury Committee](\n* [A Pilot League (Treasury Committee)](",
                "Snapshot criteria and benefits for winning communities are described in the [announcement post](",
                "The following is an extract of the proposal posted on the [Idle governance forum](",
            ],
            "decentralgames.eth": [
                "Following a passed governance proposal",
                "Details of the DCL proposal:",
                "(",
            ],
            "lido-snapshot.eth": [  # 직접 분류하기
                "In order to take part, check your eligibility [here](",
                "Claim with official link:",
                "Claim drop here:",
                "The full proposal is available [here](",
                "of LDO at any time).",
                "of LDO, they can sell that",
                "All reports are to be distributed through the Messari newsletter (~200k subscribers) and social channels.",

            ],
            "vote.airswap.eth": [
                "All proposals are public domain via[ CC0](",
            ],

            "unidexapp.eth": [
                "to have their reward distributed in by selecting a network and corresponding token below.",
                "to distribute their reward by selecting a network and corresponding token below.",
                "and it should be noted",
                "you are not voting for someone else's destination chain.",
                # "control which chain you want YOUR rewards sent to.",
                "This vote allows you to",
                'This "vote" allows you to',
                'This "vote" lets you',
            ],
            "gov.radworks.eth": [
                "* Please formally review the [official draft]( of the RGP proposal on Discourse before voting. It includes full details on the proposed program structure and implementation. *",
            ],
            "alchemixstakers.eth": [
                "Please read the full proposal here:",
                "(Learn more about our vision [here](",
                "Read more about it [here](",
            ],
            "bancornetwork.eth": [
                "Token Address:",
                "Project Website:",
                "[Read the original proposal on Discourse](",
                "[Original Proposal](",
                "Read the original proposal on [Discourse](",
                "This proposal is expected to appear on Snapshot for voting on",
                "[Daniel Luca Audit](",
                "[Mudit Gupta](",
                "Make sure to stake your vBNT for voting before this date and time to participate in the DAO decision.",

            ],
            "poh.eth": [
                "Forum discussion:",
                "English version",
            ],
            "banklessvault.eth": [
                "You can read the [full specification here](",
                "[Forum Post](",
            ],
            "qidao.eth": [  # 직접 분류하기 좋음
                "*Please read the entire proposal before voting, as there are several factors to consider.*",
            ],
            "stakewise.eth": [  # 직접 분류하기 좋음
                "Description and discussions about the proposal are available at",
            ],
            "snapshot.dcl.eth": [
                "This proposal is summarized due to technical limitations. To view it complete and vote on it, visit the DCL DAO Governance dApp",
                "Should the following ", ": up to $",
                "months vesting (1 month cliff) grant in the ",
                "one-time payment grant in the ",
                "grant in the ",
                "be approved?",

                "Email address",
                "Relevant Links",
                "> by",
                "*[Vote on this proposal on the Decentraland DAO](",
                "Manager Addresses",
                "(Zino)", "(Huepow)", "(Yemel)",
                "[]"
            ],

            "frax.eth": [  # "notng"는 줄임말 같다...?
                "Authors\nFrax Core Team", "Author\nFrax Core Team",
                "*Authors*\nFrax Core Team",
                "Author\nC2tP (Convex Finance)", "*Author*\nC2tP (Convex Finance)",
                "Author\nDeFi Dave",
                "Author\nHameed",
                "Authors\nJason Huan, Dennis, Sam Kazemian",
                "And you can read more about it",
                "[here](", "[here ]("
            ],
            "ampleforthorg.eth": [
                "Submitted via Twitter by:",
            ],
            "unlock-protocol.eth": [
                "Please check details about contributions on this thread.",
                "Nomination:",
                "To vote with the above in mind, please review each of the nominations via the discourse link:",
            ],
            "cakevote.eth": [  # Max Stake per Wallet:
                "Please refer to the following [*link*]( for migration instructions",
                "(Figures are for illustration purposes only.)",
                "Refer to the [*IFO participation guide*]( and [*iCAKE article*](",
            ],
            "1inch.eth": [
                "*Author:* [carlosjmelgar](",
            ],
            "ffdao.eth": [
                "A comprehensive scorecard breakdown can be viewed [here](",
                "A comprehensive breakdown of the scorecard can be viewed [here](",
                "Author\nCarlos Gomes",
                "Author\npastacartel",
            ],
            "shapeshiftdao.eth": [  # Team
                "The details below expand upon the [budget spreadsheet](",
            ],
            "buzzedbears.eth": [
                "*:*", "Author(s): Mesk85.eth, defijesus.eth, Felfire",
            ],
            "sharkdao.eth": [
                "*Authors:* ,",
            ],
            "0xgov.eth": [
                "Forum post:",
            ],
            "mainnet.ssvnetwork.eth": [  # 그냥 분류해도 될 듯
                "In case of urgent questions here are my contacts:",
                # "Company/requester\n* TableStakes"
                # Company/Requestor
            ],

            "dydxgov.eth": [
                "In reference to:",
                "In reference to this discussion:",
                "Calling all dydx users!",
                "We're delighted to share the exciting news that ",
                "Dive into the specifics below to learn about the launch date and the transformative changes it holds for our vibrant community.",
                "Take a moment to check your eligibility for a potential Airdrop by exploring additional details [HERE]( Seize this golden opportunity to become an integral part of the dynamic developments unfolding within the dydx community!",
            ],
            "latticegov.eth": [
                "Please carefully read the proposal thread on the governance forum before you vote:",
            ],

            "arbitrumfoundation.eth": [
                "link to application",
                "link to initial stip application:\nlink to addendum:",
            ],

            "cvx.eth": [
                "Please read gauge voting rules before voting:",
                "Be sure to also consult the voting dashboard for gauge voting insights:",
                "Authors\nFrax Core Team", "Author\nFrax Core Team",
                "Author\nC2tP (Convex Finance)",
                "Each pair is an isolated, permission-less market that allows anyone to create and participate in lending and borrowing activities.",
                "So far, we have deployed multiple AMOs, including lending AMOs on the Fraxlend, Aave, and Rari protocols.",
            ],
            "synapseprotocol.eth": [
                "For more context:",
            ],
            "aladdindao.eth": [
                "Please select NOT MORE THAN 3 members at the bottom",
                "Here is the *Boule Members* introduction:",
                "For more details, please refer to:",
                "*Further details of the proposal and discussion are here:*",
                "including holders of ALD LP positions and unclaimed ALD from LP, farming positions, or contributor allotments.",
                "You find more info about Jeff Tang in his forum post:",
                "Further details and discussion are available in the Aladdin forum:",
                "As [*announced*]( to the community,",
                "Extra juicy!",
            ],
            "bullsontheblock.eth": [  # https://snapshot.org/#/bullsontheblock.eth/proposal/0x3608e288ba411b2c6f7f65c4195665ab603823e94af22a99bdc6de23bb2cf0b1
                "IMPORTANT NOTE: The BOTB DAO Snapshot is a mirrored version of the ApeCoin DAO Snapshot.",
                "Link to the full proposal:",
                "*The AIP implementation is administered by the Ape Foundation. Implementation may be immaterially or materially altered to optimise for security, usability, to protect APE holders, and otherwise to effect the intent of the AIP. Any material deviations from an AIP, as initially approved, will be disclosed to the APE holder community.*",
                "BOTB Holders may cast their vote via BOTB DAO Snapshot. All BOTBs are encouraged to thoroughly understand the proposal prior to casting votes in order to make neutral and well-informed decisions.",
                "[Please continue reading the rest of this AIP on the ApeCoin DAO Snapshot and Discourse]",
                "Read, research, discuss - See what you think, fellow BOTBs! Make your voices heard.",
                "**",
            ],
            "jbdao.eth": [
                "[Discussion Thread]( | [IPFS](",
                "*Author:*",
                "See this proposal on IPFS",
                "Discord Discussion",
                "Notion Proposal",
            ],
            "bitdao.eth": [
                "This proposal is", "co-authored by", "authored by",
                "[cateatpeanut](",
                "the Mantle Economics Committee ([MIP-25](",
                "Mirana Ventures and the Mantle Core Contributor Team.",
            ],
            "doodles.eth": [
                "Doodle ID for Kudos:",
                "Doodle ID for kudos:",
                ">", "**",
            ],
            "pushdao.eth": [  # 직접 분류하기 좋음
                "1. Go to [",
                "2. Email",
                "Link to the Proposal Draft on Governance Forum:",
                "10. Wallet Address",
                "*[Link to Forum Discussion](",
                "Link to Forum Discussion",
            ],
            "grailers.eth": [
                "Authors:",
                "As discussed in channel",
            ],
            "beanstalkfarms.eth": [
                "Proposer\nBeanstalk Farms",
            ],
            "anglegovernance.eth": [
                "Please read Liquidity Mining weights voting rules before voting:",
                "Be sure also to engage in the",
            ],
            "bestfork.eth": [
                "Link to [WIP",
            ],
            "krausehouse.eth": [
                "This contributor may submit a request for *up to* the specified amount based on self-assessment of their work.",
            ],
            "gearbox.eth": [  # 직접 분류하기 좋음
                "Author:", "*Author*",
            ],
            "hbot.eth": [
                "3, and",
            ],
            "notional.eth": [
                "Links",
                "The related NRC community discussion can be found here:",
                "Governance parameter documentation:",
                "* [Notional V3 docs](",
                "* [V3 Risk docs](",
                "* [V3 Technical docs](",
                "* [V3 Dune dashboard ](",
            ],
            "dappradar.eth": [
                "Co-authored by:",
            ],
            "gmdao.eth": [
                "*Author:*",  # "*Sponsors:*"
            ],
            "goldfinch.eth": [
                "Proposal discussion:",
            ],
            "vote.vitadao.eth": [
                ", you, the VITA token holders,",
                "[Slide Deck](",
            ],
            "tomoondao.eth": [
                "Please read the entire proposal before voting",
                "Please read the full details before voting:",
                "Key Results for Objective",
                "Key for Objective",
                "Objectives and Key Results:",
            ],
            "golflinks.eth": [
                "Proposal Name: [Proposal",
            ],
            "futera.eth": [  # 마지막 짧은 문장 삭제해도 될 듯
                "Choose your favourite from:",
            ],
            "floordao.eth": [  # 직접 분류하기 좋음
                "- Discord: [FloorDAO](",
                "- [Forum](",
                "- [FloorDAO twitter](",
            ],
            "venus-xvs.eth": [
                "[Finalist",
            ],
            "threshold.eth": [
                "Rules for the elections are available here:",
            ],
            "alpacafinance.eth": [
                "3 (or", "Ref to discussion thread:",
            ],
            "thelanddaoprop.eth": [
                "Proposal by",
            ],
            "cow.eth": [
                "[Simulation link](",
                "[Link to Tenderly simulation](",
                "([link](",
                "- JSON file hosted on IPFS",
                "- Core team: ``"
            ],
            "foundersdao.eth": [
                "& danielg", "sAndElf", "bennydlowkey", "Macdad", "averagejocrypto",
                "CryptoScottie", "verbdan", "Mutant Ape", "and Zeekay",
                "Details of Mechanics:"
            ],
            "apecoin.eth": [  # 결국 zero cost로 끝나는 게 많음
                "Link to the full proposal:",
                "Link to the Nomination Announcement:",
                "Link to the Nomination Profiles:",
                "*The AIP implementation is administered by the Ape Foundation. Implementation may be immaterially or materially altered to optimise for security, usability, to protect APE holders, and otherwise to effect the intent of the AIP. Any material deviations from an AIP, as initially approved, will be disclosed to the APE holder community.*",
                "IMPORTANT NOTE: The BOTB DAO Snapshot is a mirrored version of the ApeCoin DAO Snapshot.",
                "BOTB Holders may cast their vote via BOTB DAO Snapshot.",
                "All BOTBs are encouraged to thoroughly understand the proposal prior to casting votes in order to make neutral and well-informed decisions.",
            ],
            "benddao.eth": [
                "- [Snapshot]( - [Forum Proposal](",
            ],
            "theholyones.eth": [
                "Also, if you rather discuss in private, ask me in general chat to add you as a friend so you can direct message me."
            ],
            "metislayer2.eth": [
                "Thank you for your consideration!",
                "Hi Metisians", "This is the time!",
                "Official Links: Website, Docs, Audits, etc.",
            ],
            "muuu.eth": [
                "Please read the document to understand gauge voting rules before voting.",
                "After the voting in SnapShot is done, the Muuu Finance team will vote for Kagla Finance.",
            ],
            "metfi.io": [
                "vote-discussion channel.",
            ],
            "beanstalkdao.eth": [
                "Proposer Wallet: (",
            ],
            "aurafinance.eth": [
                "[PR with Payload](",
                "PR with Payload",
                "References/Useful links:",
                "Please read gauge voting rules before voting:",
                "Be sure to also consult the voting dashboard for gauge voting insights:"
            ],
            "leagueoflils.eth": [
                "createdTransactionHash -",
            ],
            "rocketpool-dao.eth": [
                "[Full RPIP](", "[Forum thread](",
                "- [Ongoing forum conversation](",
                "- Selected discord discussions: [1]( [2](",
            ],
            "kalmyapp.eth": [  # 직접 분류하기 좋음
                "Read about the specific calculations used in this blog:",
                "- [Visit our Website](\n- [Follow us on Twitter (X)](\n- [DeFi Wars - Vault Request Form](",
            ],
            "safe.eth": [
                "Please refer to the [full proposal text on the SafeDAO forum]( Some parts may have been removed to fit within the character limit on Snapshot.",
                "*Below information is only a summary, the whole proposal with the full description is available here:",
                "Authors:",
            ],
            "conic-dao.eth": [
                "Please read the LAV voting rules before voting:",
                "Be sure to also consult the current Curve pool distribution found on the Conic Omnipool page for insights:",
                "Before voting please read the full proposal on Discourse:",
            ],
            "gauges.aurafinance.eth": [
                "Please read gauge voting rules before voting:",
                "Be sure to also consult the voting dashboard for gauge voting insights:"
            ],
            "arbitrumfoundation.eth": [
                "This is a proposal for the [Arbitrum Short-Term Incentives Program]( you can find the details of this specific protocols proposal in the forum link attached below.",
                "Link to Application",
                "*Who proposed this challenge:*",
                "*Why this request needs a closer look:*",
                "*Link to initial STIP application:*",
                "*Link to Addendum:*",
                "*ARB Requested:*"
            ],
            "chaingptai.eth": [
                "The information provided is for informational purposes only and should not be considered legal, financial, or investment advice. Participants should consult professionals and conduct their own research before engaging in any activities. The project team and organizers are not responsible for any financial losses or legal consequences. Participation in this DAO proposal and potential event is restricted for residents of the following countries: USA, Canada, Tunisia, Qatar, Nepal, Morocco, Iraq, Egypt, China, Bangladesh, Algeria. Participants should not expect any profits or increased value of the utility token CGPT from this event."
            ],
            "equilibriafi.eth": [
                "Here are more info about"
            ],
            "dao.connext.eth": [
                "Please check the forum post.",
                # "The following provides an overview of the objectives of the Community Leaders for the upcoming quarter:",
            ],
            "hvax.eth": [
                "This temperature check will gauge delegates' interest/support for deploying the onboarding package to",
                "TokenLogic and karpatkey receive no payment for this proposal. TokenLogic and karpatkey are both delegates within the Aave community.",
                "By approving this proposal, you agree that any services provided by Gauntlet shall be governed by the terms of service available at gauntlet.network/tos",
                "By approving this proposal, you agree that any services provided by", "shall be governed by the", "[Terms of Service](", "that were updated as of",
                "[Full proposal and forum discussion](",
                "- Implementation: [AaveV3Ethereum](",
                "- Tests: [AaveV3Ethereum](",
                "- [Snapshot](",
                "- [Discussion](",
                "**",
            ],
            "gauges.equilibria-xeqb.eth": [
                "Here are more info about",
            ],
            "cryptomods.eth": [
                "[Please review the relevant discussion for this proposal in r/CryptoCurrencyMeta before voting. A copy of the body text for the proposal can be found below.](",
                "*As a reminder, if two concurrent proposals are conflicting or impacting the same mechanism then only the one with the most votes in favor will be passed.*",
            ]
        }
    }

}
