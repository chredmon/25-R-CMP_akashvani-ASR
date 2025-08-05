#!/home/cr/Documents/sources/julia-1.11.6/bin/julia 
# Download websites with news bulletin information from newsonair.gov.in 
# Charles Redmon
# 2025-08-01

# load external packages
using Printf
using HTTP 

# configure arguments
ntype = ARGS[1];
istart = parse(Int, ARGS[2]);
iend = parse(Int, ARGS[3]);

if ntype == "audio"
    baseurl = "https://www.newsonair.gov.in/bulletins-category/regional-audio/";
elseif ntype == "text"
    baseurl = "https://www.newsonair.gov.in/bulletins-category/regional-text/";
else 
    error("ERROR: No valid news type given (must be 'audio' or 'text').")
end


# dirs
outdir = "../data/raw/html/"

# main loop

for i=istart:iend 

    println(string("Downloading page ", string(i), "..."))

    inurl = string(baseurl, "?page=", string(i));
    outurl = string(outdir, ntype, "-", @sprintf("%04d", i), ".html");

    f = open(outurl, "w");
    r = HTTP.get(inurl, response_stream=f);
    close(f);

end 




