TOP20 = [
    "0xgov.eth",
    "1inch.eth",
    "aave.eth",
    "aavegotchi.eth",
    "arbitrumfoundation.eth",
    "badgerdao.eth",
    "balancer.eth",
    "comp-vote.eth",
    "cvx.eth",
    "curve.eth",
    "dydxgov.eth",
    "ens.eth",
    "frax.eth",
    "olympusdao.eth",
    "opcollective.eth",
    "cakevote.eth",
    "radiantcapital.eth",
    "suchigov.eth",
    "graphprotocol.eth",
    "uniswapgovernance.eth"
]

class DAO:
    def fetch_spaces(self, skip:int=0) -> str:
        return """ query Spaces{
                      spaces(
                  first: 1000,
                  skip: %d,
                  orderBy: "created",
                  orderDirection: asc
              ) {
              created
            id 
          name 
          skin 
          rank 
          about 
          terms 
          email 
          turbo 
          boost {
            enabled
            bribeEnabled
          } 
          avatar 
          github 
          symbol 
          domain 
          admins 
          voting {
            delay
            period
            type
            quorum
            blind
            hideAbstain
            privacy
            aliased
          } 
          parent {
            id
          } 
          private 
          website 
          twitter 
          network 
          members 
          filters {
            minScore
            onlyMembers
          } 
          plugins 
          flagged 
          created 
          location 
          children {
            id
          } 
          template 
          verified 
          coingecko 
          strategies {
            network
            params
          } 
          moderators 
          categories 
          validation {
            params
          } 
          treasuries {
            name
            address
            network
          } 
          votesCount 
          guidelines 
          hibernated 
          __typename 
          votesCount7d 
          voteValidation {
            params
          } 
          proposalsCount 
          followersCount 
          activeProposals 
          delegationPortal {
            delegationType
            delegationApi
            delegationContract
          }
          proposalsCount7d 
          followersCount7d
            }}
        """ % skip
  

    def fecth_proposals(self, space:str, skip:int=0) -> str:
        return """
                        
          query Proposals {
            proposals (
              first: 1000,
              skip: %d,
              where: {
                space_in: ["%s"],
              },
              orderBy: "created",
              orderDirection: desc
            ) {
              
          id
          end
          app
          ipfs
          type
          body
          link
          space {
            id
          }
          title
          start
          state
          votes
          author
          symbol
          quorum
          scores
          created
          updated
          network
          plugins
          choices
          privacy
          flagged
          snapshot
          strategies {
            network
            params
          }
          validation {
            params
          }
          discussion
          quorumType
          __typename
          scores_state
          scores_total
          scores_updated
          scores_by_strategy
            }
          }
        """ % (skip, space)
    
    def fetch_votes(self, proposal_id:str, skip:int=0, ) -> str:
      return """
      query Votes {
        votes(
          first: 1000, 
          skip: %d, 
          where: {proposal: "%s"}, 
          orderBy: "created", 
          orderDirection: desc) 
        {
          id
          vp
          app
          ipfs
          voter
          space {
            id
          }
          choice
          reason
          created
          proposal {
            id
          }
          metadata
          vp_state
          __typename
          vp_by_strategy
        }
      }
      """ % (skip, proposal_id)