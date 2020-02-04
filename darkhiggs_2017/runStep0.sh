for f in crab_cfg_dark*.py
do
    crab submit -c $f
done

