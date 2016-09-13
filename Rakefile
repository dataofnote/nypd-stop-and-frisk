require 'pathname'
WRANGLE_DIR = Pathname 'wrangle'
CORRAL_DIR = WRANGLE_DIR / 'corral'
SCRIPTS = WRANGLE_DIR / 'scripts'

DIRS = {
    'fetched' => CORRAL_DIR / 'fetched',
    'homogenized' => CORRAL_DIR / 'homogenized',
    'compiled' => CORRAL_DIR / 'compiled',
    'published' =>  Pathname('data'),
}

START_YEAR = 2003
END_YEAR = 2015 # data is updated on an annual basis, so this file
                # can be manually edited

F_FILES = (START_YEAR..END_YEAR).map{|y| DIRS['fetched'].join("#{y}.csv") }
H_FILES = F_FILES.map{|p| DIRS['homogenized'] / p.basename }
C_FILES = F_FILES.map{|p| DIRS['compiled'] / p.basename }


desc 'Setup the directories'
task :setup do
    DIRS.each_value do |p|
        p.mkpath()
        puts "Created directory: #{p}"
    end
end


desc "Fetch all yearly CSV files."
task :fetch do
    F_FILES.each{|fn| Rake::Task[fn].invoke() }
end

desc "Homogenize the fetched yearly CSV files"
task :homogenize => :setup do
    H_FILES.each{|fn| Rake::Task[fn].invoke() }
end

desc "Clean up the fields, derive proper values"
task :compile => :setup do
    C_FILES.each{|fn| Rake::Task[fn].execute() }
end



C_FILES.each do |destname|
    srcname = DIRS['homogenized'] / destname.basename
    desc "#{destname.basename} CSV file with cleaned headers and data"
    file destname => srcname do
        year = destname.basename.to_s[/\d{4}/]
        cmd = ['python', SCRIPTS.join('derive.py'),
                  srcname,
                  'derive_yesno',
                  'derive_force_type_used',
                  'derive_weapon_type_found',
                  'derive_latlng',
                  'derive_datetime_stop',
                  '>', destname]
        sh cmd.join(' ')
    end
end

## File listing
H_FILES.each do |destname|
    srcname = DIRS['fetched'] / destname.basename
    desc "#{destname.basename} CSV file with homogenized headers"
    file destname => srcname do
        year = destname.basename.to_s[/\d{4}/]
        cmd = ['python', SCRIPTS.join('homogenize.py'),
                  srcname, year, '>', destname]
        sh cmd.join(' ')
    end
end



F_FILES.each do |fname|
    desc "#{fname.basename} text file as fetched and extracted from nyc.gov"
    file fname do
        year = fname.basename.to_s[/\d{4}/]
        cmd = ['bash', SCRIPTS.join('fetch_and_unpack.sh'),
                year, '>', fname]

        sh cmd.join(' ')
    end
end





