require 'pathname'
WRANGLE_DIR = Pathname 'wrangle'
CORRAL_DIR = WRANGLE_DIR / 'corral'
SCRIPTS_DIR = WRANGLE_DIR / 'scripts'

DIRS = {
    :fetched => CORRAL_DIR / 'fetched',
    :homogenized => CORRAL_DIR / 'homogenized',
    :published =>  Pathname('data'),
}

START_YEAR = 2003
END_YEAR = 2015 # data is updated on an annual basis, so this file
                # can be manually edited

F_FILES = (START_YEAR..END_YEAR).map{|y| DIRS[:fetched].join("#{y}.csv") }
H_FILES = F_FILES.map{|p| DIRS[:homogenized] / p.basename }

desc 'Setup the directories'
task :setup do
    DIRS.each_value do |p|
        p.mkpath()
        puts "Created directory: #{p}"
    end
end


namespace :publish do
    desc "Fetch all yearly CSV files."
    task :fetch do
        F_FILES.each{|fn| Rake::Task[fn].invoke() }
    end

    desc "Homogenized the fetched yearly CSV files"
    task :homogenize => :setup do
        H_FILES.each{|fn| Rake::Task[fn].invoke() }
    end
end


## File listing
H_FILES.each do |destname|
    srcname = DIRS[:fetched] / destname.basename
    desc "#{destname.basename} CSV file with homogenized headers"
    file destname => srcname do
        year = destname.basename.to_s[/\d{4}/]
        cmd = ['python', SCRIPTS_DIR.join('homogenize.py'),
                  srcname, year, '>', destname]
        sh cmd.join(' ')
    end
end



F_FILES.each do |fname|
    desc "#{fname.basename} text file as fetched and extracted from nyc.gov"
    file fname do
        year = fname.basename.to_s[/\d{4}/]
        cmd = ['bash', SCRIPTS_DIR.join('fetch_and_unpack.sh'),
                year, '>', fname]

        sh cmd.join(' ')
    end
end





