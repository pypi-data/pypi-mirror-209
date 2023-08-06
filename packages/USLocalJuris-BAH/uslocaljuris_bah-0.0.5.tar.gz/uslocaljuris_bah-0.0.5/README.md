
us states and localities: a modification of the us package
=====================================

A package for easily working with US state and select locality metadata.

### New: 

* Kansas City, MO
* Soon: largest cities/villages and towns from New York State excluding NYC
* Names
* Census GEOID
* what state they are part of
* time zone
* what state they are part of
* is contiguous or continental
* Goal: shape file of precincts/remainder (or guestimated precint info) shape files 
  from 2020 Census

### Old:

* all US states and territories
* postal abbreviations
* Associated Press style abbreviations
* FIPS codes
* capitals
* years of statehood
* time zones
* phonetic state name lookup
* is contiguous or continental
* URLs to shapefiles for state, census, congressional districts,
  counties, and census tracts from the 2010 Census


Installation
------------
For Unix/Mac computers:

    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps USLocalJuris-BAH


Features
--------

Easy access to state information: ::

    >>> import us
    >>> us.states.MD
    <State:Maryland>
    >>> us.states.MD.fips
    u'24'
    >>> us.states.MD.name
    u'Maryland'
    >>> us.states.MD.is_contiguous
    True

Includes territories too: ::

    >>> us.states.VI.name
    u'Virgin Islands'
    >>> us.states.VI.is_territory
    True
    >>> us.states.MD.is_territory
    False

List of all (actual) states: ::

    >>> us.states.STATES
    [<State:Alabama>, <State:Alaska>, <State:Arizona>, <State:Arkansas>,...
    >>> us.states.TERRITORIES
    [<State:American Samoa>, <State:Guam>, <State:Northern Mariana Islands>,...

And the whole shebang, if you want it: ::

    >>> us.states.STATES_AND_TERRITORIES
    [<State:Alabama>, <State:Alaska>, <State:American Samoa>,...

For convenience, `STATES`, `TERRITORIES`, and `STATES_AND_TERRITORIES` can be
accessed directly from the `us` module: ::

    >>> us.states.STATES
    [<State:Alabama>, <State:Alaska>, <State:Arizona>, <State:Arkansas>,...
    >>> us.STATES
    [<State:Alabama>, <State:Alaska>, <State:Arizona>, <State:Arkansas>,...

There's also a list of obsolete territories: ::

    >>> us.states.OBSOLETE
    [<State:Dakota>, <State:Orleans>, <State:Philippine Islands>]

The state lookup method allows matching by FIPS code, abbreviation, and name: ::

    >>> us.states.lookup('24')
    <State:Maryland>
    >>> us.states.lookup('MD')
    <State:Maryland>
    >>> us.states.lookup('md')
    <State:Maryland>
    >>> us.states.lookup('maryland')
    <State:Maryland>

Get useful information: ::

    >>> state = us.states.lookup('maryland')
    >>> state.abbr
    u'MD'


And for those days that you just can't remember how to spell Mississippi,
we've got phonetic name matching too: ::

    >>> us.states.lookup('misisipi')
    <State:Mississippi>


Shapefiles
----------

You want shapefiles too? Gotcha covered.

::

    >>> shpurls = us.states.MD.shapefile_urls()
    >>> for region, url in shpurls.items():
    ...   print "%s: %s" % (region, url)
    ...
    county: http://www2.census.gov/geo/tiger/TIGER2010/COUNTY/2010/tl_2010_24_county10.zip
    state: http://www2.census.gov/geo/tiger/TIGER2010/STATE/2010/tl_2010_24_state10.zip
    cd: http://www2.census.gov/geo/tiger/TIGER2010/CD/111/tl_2010_24_cd111.zip
    zcta: http://www2.census.gov/geo/tiger/TIGER2010/ZCTA5/2010/tl_2010_24_zcta510.zip
    tract: http://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_24_tract10.zip

The `shapefile_urls()` method on the State object generates shapefile URLs for
the following regions:

* state
* county
* congressional district
* zcta
* census tract

If you know what region you want, you can explicitly request it: ::

    >>> us.states.MD.shapefile_urls('county')
    u'http://www2.census.gov/geo/tiger/TIGER2010/COUNTY/2010/tl_2010_24_county10.zip'


Mappings
--------

Mappings between various state attributes are a common need. The `mapping()`
method will generate a lookup between two specified fields.

::

    >>> us.states.mapping('fips', 'abbr')
    {u'30': u'MT', u'54': u'WV', u'42': u'PA', u'48': u'TX', u'45': u'SC',...
    >>> us.states.mapping('abbr', 'name')
    {u'WA': u'Washington', u'VA': u'Virginia', u'DE': u'Delaware',...


CLI
----

When you need to know state information RIGHT AWAY, there's the *states* script.

::

    $ states md

    *** The great state of Maryland (MD) ***

      FIPS code: 24

      other attributes:
        ap_abbr: Md.
        capital: Annapolis
        capital_tz: America/New_York
        is_obsolete: False
        name_metaphone: MRLNT
        statehood_year: 1788
        time_zones: America/New_York

      shapefiles:
        blockgroup: http://www2.census.gov/geo/tiger/TIGER2010/BG/2010/tl_2010_24_bg10.zip
        cd: http://www2.census.gov/geo/tiger/TIGER2010/CD/111/tl_2010_24_cd111.zip
        county: http://www2.census.gov/geo/tiger/TIGER2010/COUNTY/2010/tl_2010_24_county10.zip
        state: http://www2.census.gov/geo/tiger/TIGER2010/STATE/2010/tl_2010_24_state10.zip
        tract: http://www2.census.gov/geo/tiger/TIGER2010/TRACT/2010/tl_2010_24_tract10.zip
        zcta: http://www2.census.gov/geo/tiger/TIGER2010/ZCTA5/2010/tl_2010_24_zcta510.zip
        block: http://www2.census.gov/geo/tiger/TIGER2010/TABBLOCK/2010/tl_2010_24_tabblock10.zip


Running Tests
-------------

CircleCI is set up to automatically run unit tests against any new commits to
the repo. To run these tests yourself in a standardized, Dockerized
environment, install
`the CircleCI CLI <https://circleci.com/docs/2.0/local-cli/>`_, and then
execute the tests with: ::

    circleci local execute --job build

Alternatively, you can run tests against only your current version of Python,
using: ::

    pytest tests


Changelog
---------

0.0.5
~~~~~

* fixed README text somewhat

0.0.4
~~~~~

* missing comma in Kansas City
* milestone: importing without error

