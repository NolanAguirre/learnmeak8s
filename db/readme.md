# Database
the database is postgres managed with sqitch 

0.0.0 is the util schema, a set of functions that are meant to help out in database development. Im going to be building it out over time, I will not be using rework to do this, Im just going to change the file.


## Nameing 
The naming is not for best lexical sort, and is not for strict versioning, its lexical sort while being memorable enough to talk about and use elsewhere, timestamps are not useable in this way. Saying "Oh! migration 1.30 implemented that feature! is pretty useful"

The naming of the db is a version of <major>.<minor>.<patch>, but you probably won't use major versions as breaking compatabiltiy to that degree shouldn't be common. Patches should be fixes to a spcific feature that is implemented in a single minor verions change, if the feature spans two minor versions things get weird. A minor version change is a feature basically, all db changes needed for a deployment to production to enable a feature. Patches aren't always super useful because a bug might span several minor versions leaving no clear minor version to increment the patch on. I've never seen a situation so odd it wasn't serviced by: if the bug is isolated in one minor version, use a patch, otherwise it is likely an issue that requires a minor version increase anyway, so just use a new minor version that has the correct dependencies in sqitch.

Major goes to 0-9, see major versions later. It wont happen often, I like short names

Minor goes to 0-999 because if you get to 999 features implemented then its probably time to compress the db migrations, tbh 99 is probably enough but I've seen it before so another zero it is. Its really anoying when your very nice sorted directory becomes messy because you implmented the 100th feature.

Patch goes to -=9 because I want the names to be short, typeing 3 zeros for minor is enough for me. If you cant fix a bug in 9 tries, well something else is wrong, its not worth having a bunch of extra zeros in the file name.


## Dependencies
The naming is sqitch is really supposed to order correctly, the dependencies provided via --requires need to be correct regardless. Generally minor versions don't really need to have the correct dependencies but there are some very odd edge cases that handle existing data that could cause issues, so make sure you add them even though the naming orders things.

### Major versions
Major versions have two main usages, being a true major version update, say numeric ids to uuids, changing schema/core table names, probably some others. The other usage is you reach the 999 feature minor versions. If this happens, you likely have too many db migrations to make sense, they should be compressed into a single migration and basically snapshotted into a new major version. The old 999+ migrations can then be thrown out. Think of it like distributed messaging pruning, we're dropping the migrations that never make it to the running state of the database. In postgres you can use the catalog tables to do this kind of compression, the catalog tables can be queried and the structure of the currently running database can be returned.




## Util schema
Minor version in the util schema will likely be for different environments, you'll choose to include them based on your starting infrastructure. Right now there is only one, an optional util package that enables postgraphile.