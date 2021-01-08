#graph body is dictionary/hashtable <key, array>
graph = {}
#start node
graph["you"] = ["alice", "bob", "claire"]
#first level nodes
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
#second level nodes
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []